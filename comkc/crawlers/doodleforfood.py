# -*- coding: utf-8 -*-
import logging
import re

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)

re_img = re.compile(r'<\s*img \s*src="([^"]+)"\s*/>')


class Worker(BaseWorker):
    SITE = 'Doodle for Food'
    BASE_URL = 'http://www.doodleforfood.com/rss'

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = await self.parse_rss_items(html)

        for item in data:
            description = item['description']
            image_url = pq(description)('img').attr('src')
            item.update({
                'title': '{0} - {1}'.format(self.SITE, item['title']),
                'url': item['link'],
                'date': item['pubDate'],
                'image': image_url,
            })
        return data

    async def parse_item(self, url):
        await asyncio.sleep(0)
        return {}


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
