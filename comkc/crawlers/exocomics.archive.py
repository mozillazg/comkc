# -*- coding: utf-8 -*-
import datetime
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Extra Ordinary'
    BASE_URL = 'http://www.exocomics.com/archive'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = []
        for item in pq(html)('.archive')('a'):
            url = pq(item).attr('href')
            title = url.strip('/').split('/')[-1]
            data.append({
                'title': '{0} #{1}'.format(self.SITE, title),
                'url': url,
            })
        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('.main a.comic img:first').attr('src')
        date_str = pq(html)('.comment-style-admin')('.date').text().strip()
        if not date_str:
            date_str = pq(html)('.list-style-comments')('.date').text().strip()
        date_lst = date_str.replace("'", '').split()
        date_str = '{0} {1} 20{2}'.format(*date_lst)
        date = datetime.datetime.strptime(date_str, '%d %b %Y')
        return {'image': image, 'date': date}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
