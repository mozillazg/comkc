# -*- coding: utf-8 -*-
import datetime
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Berkeley Mews'
    BASE_URL = 'http://www.berkeleymews.com/?page_id=2'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        tags = pq(html)('#page table td a')
        items = []

        for tag in tags:
            item = pq(tag)
            title = item.text().strip()
            url = item.attr('href')
            items.append({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': url,
            })
        return items

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('#comic img').attr('src')
        date_str = image.split('/')[-1]
        date = datetime.datetime(*[int(x) for x in date_str.split('-')[:3]])
        return {'image': image, 'date': date}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
