# -*- coding: utf-8 -*-
import datetime
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Don\'t Hit Save'
    BASE_URL = 'http://www.donthitsave.com/archive.php'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        tags = pq(html)('.archivetable td ul li')
        items = []

        for tag in tags:
            item = pq(tag)
            date_str = item.text().split('-')[0].strip()
            date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
            tag_a = item('a')
            title = tag_a.text().strip()
            url = tag_a.attr('href')
            items.append({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': url,
                'date': date,
            })
        return items

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('head meta[property="og:image"]').attr('content')
        return {'image': image}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
