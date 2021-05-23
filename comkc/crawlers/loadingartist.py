# -*- coding: utf-8 -*-
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Loading Artist'
    BASE_URL = 'https://loadingartist.com/index.xml'
    IMAGE_URL = "https://loadingartist.com"
    ENABLE = True

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = await self.parse_rss_items(html)

        for item in data:
            title = item['title']
            item.update({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': item['link'],
                'date': item['pubDate'],
            })
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('.main-image-container picture img').attr('src') or ''
        if image and not image.startswith('http'):
            image = '{}{}'.format(self.IMAGE_URL, image)
        return {'image': image}


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
