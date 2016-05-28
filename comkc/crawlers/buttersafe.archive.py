# -*- coding: utf-8 -*-
import datetime
import logging
import re

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)

re_url = re.compile(r'https?://buttersafe\.com/(?P<date>\d{4}/\d{2}/\d{2})/')


class Worker(BaseWorker):
    SITE = 'Buttersafe'
    BASE_URL = 'http://buttersafe.com/archive/'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = []
        for ele in pq(html)('#column td.archive-title a'):
            ele = pq(ele)
            url = ele.attr('href')
            date_str = re_url.match(url).group('date')
            date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
            title = ele.text().strip()
            data.append({
                'source': url,
                'title': '{0}: {1}'.format(self.SITE, title),
                'date': date,
            })
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('#comic img').attr('src')
        return {'image': image}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
