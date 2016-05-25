# -*- coding: utf-8 -*-
import datetime
import functools
import logging

from aiopg.sa import create_engine
import xmltodict

from comkc import config
from comkc.models import table_comic, insert_comic, get_comic
from comkc.utils import fetch_url  # noqa

crawlers = {}
logger = logging.getLogger(__name__)
dsn = config.PG_DSN


async def url_is_exists(url):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            comic = await get_comic(
                        conn, table_comic.c.source == url
                    )
            if comic is not None:
                return True


async def save_data(data):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            return await insert_comic(conn, data)


async def parse_rss_items(html):
    rss_items = xmltodict.parse(html)['rss']['channel']['item']
    data = []

    for item in rss_items:
        date_str = item['pubDate']
        date = datetime.datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
        item.update({
            'pubDate': date,
        })
        data.append(item)
    return data


async def save_item(site, url, item):
    db_data = {
        'site': site,
        'title': item['title'],
        'source': url,
        'image': item['image'],
        'posted_at': item['date'],
    }
    logger.debug('got item:\n{}'.format(dict(db_data)))
    if not item['image']:
        return
    await save_data(db_data)
    logger.info('saved {}'.format(url))


def register(func):
    name = func.__module__
    crawlers[name] = func

    @functools.wraps(func)
    def _wrapper(conn, handler):
        return func(conn, handler)
    return _wrapper
