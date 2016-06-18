# -*- coding: utf-8 -*-
import asyncio
import datetime
import logging
import urllib

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Explosm'
    BASE_URL = 'http://explosm.net/comics/archive'
    ENABLE = False

    async def _get_one_month(self, url):
        html = await self.fetch_url(url)
        items = []
        for item in pq(html)('.archive-list-item .meta-data h3 a'):
            item = pq(item)
            date = datetime.datetime.strptime(item.text().strip(), '%Y.%m.%d')
            detail_url = item.attr('href')
            sn = detail_url.strip('/').split('/')[-1]
            title = 'Cyanide & Happiness #{}'.format(sn)
            items.append({
                'title': title,
                'url': detail_url,
                'date': date,
            })
        return items

    async def _get_urls(self):
        html = await self.fetch_url(self.BASE_URL)
        urls = []
        for ele in pq(html)('#archive-year-accordion ul.no-bullet li a'):
            url = urllib.parse.urljoin(
                'http://explosm.net', ele.attrib['href']
            )
            urls.append(url)
        return urls

    async def get_items(self):
        data = []
        urls = await self._get_urls()
        for url in urls:
            month_data = await self._get_one_month(url)
            data.extend(month_data)
            await asyncio.sleep(3)
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('#main-comic').attr('src')
        if not image:
            return {}
        if not image.startswith('http'):
            image = 'http:' + image
        return {'image': image}

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
