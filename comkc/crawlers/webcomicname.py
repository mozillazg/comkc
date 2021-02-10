# -*- coding: utf-8 -*-
import logging
from urllib.parse import urljoin

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'webcomic name'
    SITE_URL = 'https://webcomicname.com'
    BASE_URL = 'https://webcomicname.com/rss'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = await self.parse_rss_items(html)

        for item in data:
            title = item['link']
            item.update({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': item['link'],
                'date': item['pubDate'],
            })
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('.post-content .body-text .tmblr-full img').attr('src')  # noqa
        if not image.startswith('http'):
            image = urljoin(self.SITE_URL, image)
        return {'image': image}


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
