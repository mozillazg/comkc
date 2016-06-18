# -*- coding: utf-8 -*-
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Explosm'
    BASE_URL = 'http://feeds.feedburner.com/Explosm?format=xml'

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = await self.parse_rss_items(html)

        for item in data:
            sn = item['link'].strip('/').split('/')[-1]
            item.update({
                'title': 'Cyanide & Happiness #{}'.format(sn),
                'url': item['link'],
                'date': item['pubDate'],
            })
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('#main-comic').attr('src')
        if not image.startswith('http'):
            image = 'http:' + image
        return {'image': image}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
