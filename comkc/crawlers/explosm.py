# -*- coding: utf-8 -*-
import asyncio
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import (
    register, url_is_exists, fetch_url,
    parse_rss_items, save_item
)

logger = logging.getLogger(__name__)
SITE = 'Explosm'
SLEEP = 60 * 60 * 8
BASE_URL = 'http://feeds.feedburner.com/Explosm?format=xml'


async def get_items(url):
    html = await fetch_url(url)
    data = await parse_rss_items(html)

    for item in data:
        sn = item['link'].strip('/').split('/')[-1]
        item.update({
            'title': 'Cyanide & Happiness #{}'.format(sn),
            'url': item['link'],
            'date': item['pubDate'],
        })
    return data


async def parse_item(url):
    html = await fetch_url(url)
    image = pq(html)('#main-comic').attr('src')
    if not image.startswith('http'):
        image = 'http:' + image
    return {'image': image}


@register
async def main():
    while True:
        try:
            logger.info('start fetching {}'.format(BASE_URL))
            items = await get_items(BASE_URL)
            for item in items[::-1]:
                url = item['url']
                if await url_is_exists(url):
                    logger.info('{} is exists, skip'.format(url))
                    continue

                logger.info('fetching {}'.format(url))
                item.update(await parse_item(url))
                await save_item(SITE, url, item)
                await asyncio.sleep(60 * 1)

        except Exception as e:
            logger.exception(e)
            await asyncio.sleep(60 * 2)
        else:
            await asyncio.sleep(SLEEP)
            logger.info('sleep...')
