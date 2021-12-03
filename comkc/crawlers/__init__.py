# -*- coding: utf-8 -*-
import abc
import asyncio
import datetime
import logging
import random

from aiopg.sa import create_engine
import xmltodict

from comkc import config
from comkc.models import table_comic, insert_comic, get_comic
from comkc.utils import fetch_url as _fetch_url

crawlers = {}
logger = logging.getLogger(__name__)
dsn = config.PG_DSN


class WorkerMeta(type):
    def __init__(cls, name, bases, namespace):
        site = cls.SITE
        if cls.ENABLE and site and site not in crawlers:
            crawlers[site] = cls


class BaseWorker(metaclass=WorkerMeta):
    SITE = None
    BASE_URL = None
    SLEEP = config.WORKER_SLEEP
    ENABLE = True

    def __init__(self):
        self.config = config

    @abc.abstractmethod
    async def get_items(self) -> list:
        pass

    @abc.abstractmethod
    async def parse_item(self, url) -> dict:
        pass

    async def run(self):
        while True:
            try:
                logger.info('start fetch {}'.format(self.BASE_URL))
                items = await self.get_items()
                logger.info('got {} items for {}'.format(
                    len(items), self.BASE_URL))
                for item in items[::-1]:
                    try:
                        url = item['url']
                        if await self.url_is_exists(url):
                            logger.debug('{} is exists, skip'.format(url))
                            continue

                        logger.info('fetching {}'.format(url))
                        extra_data = await self.parse_item(url)
                        logger.info('fetch {} got {}'.format(url, extra_data))
                        if extra_data is None:
                            logger.info(
                                'not found extra_data for {}, skip'.format(url)
                            )
                            continue
                        item.update(extra_data)
                        await self.save_item(self.SITE, url, item)
                        await asyncio.sleep(60 * 1 * (random.random() + 1))
                    except Exception as e:
                        logger.exception('%s %s %s', e, self.BASE_URL, item)
                        await asyncio.sleep(60 * 5 * (random.random() + 1))
            except Exception as e:
                if 'DoesNotExist' in str(e) or \
                        'page does not exist' in '{}'.format(e):
                    logger.info(e)
                    await asyncio.sleep(60 * 20 * (random.random() + 1))
                else:
                    logger.exception(e)
                    await asyncio.sleep(60 * 10 * (random.random() + 1))
            else:
                await asyncio.sleep(self.SLEEP * (random.random() + 1))
                logger.info('sleep...')

    async def __call__(self):
        return await self.run()

    @staticmethod
    async def fetch_url(url, binary=False, **kwargs):
        return await _fetch_url(url, binary=binary, **kwargs)

    @staticmethod
    async def url_is_exists(url):
        async with create_engine(dsn) as engine:
            async with engine.acquire() as conn:
                comic = await get_comic(
                            conn, table_comic.c.source == url
                        )
                if comic is not None:
                    return True

    @staticmethod
    async def save_data(data):
        async with create_engine(dsn) as engine:
            async with engine.acquire() as conn:
                return await insert_comic(conn, data)

    @staticmethod
    async def parse_rss_items(html):
        xmldict = xmltodict.parse(html)
        if 'rss' in xmldict:
            rss_items = xmldict['rss']['channel']['item']
        elif 'feed' in xmldict:
            rss_items = xmldict['feed']['entry']

        if isinstance(rss_items, dict):
            rss_items = [rss_items]

        data = []

        for item in rss_items:
            date_str = ''
            if 'pubDate' in item:
                date_str = item['pubDate']
            if 'updated' in item:
                date_str = item['updated']

            if date_str:
                try:
                    try:
                        date = datetime.datetime.strptime(
                                date_str, '%a, %d %b %Y %H:%M:%S %z')
                        item.update({
                            'pubDate': date,
                        })
                    except Exception as e:
                        # 2019-10-02T05:43:56Z
                        date = datetime.datetime.strptime(
                                date_str, '%Y-%m-%dT%H:%M:%SZ')
                        item.update({
                            'pubDate': date,
                        })
                except Exception as e:
                    logger.exception('%s %s', e, item)
            data.append(item)
        return data

    @staticmethod
    async def save_item(site, url, item):
        logger.info('start save {} {}'.format(url, item['image']))
        if isinstance(item['image'], list):
            image = ' '.join(item['image'])
        else:
            image = item['image']
        db_data = {
            'site': site,
            'title': item['title'],
            'source': url,
            'image': image,
            'posted_at': item['date'],
        }
        logger.debug('got item:\n{}'.format(dict(db_data)))
        if not item['image']:
            return
        await BaseWorker.save_data(db_data)
        logger.info('saved {}'.format(url))
