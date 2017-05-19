# -*- coding: utf-8 -*-
import datetime
import logging
import re

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Invisible Bread'
    BASE_URL = 'http://invisiblebread.com/archives/'

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        data = []

        for item in self._get_items(html):
            data.append(item)
            title = item['title']
            item.update({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': item['url'],
                'date': item['date'],
            })
        return data

    def _get_items(self, html):
        trs = pq(html)('.month-table tr')
        for tr in trs:
            yield self._parse_tr(tr)

    def _parse_tr(self, tr):
        tr = pq(tr)
        title = tr('.archive-title a').text().strip()
        link = tr('.archive-title a').attr('href')
        year = re.findall(r'/(\d{4})/', link)[0]
        month, day = tr('.archive-date').text().strip().split()
        day = '{0:0>2}'.format(day)
        date_str = '{0} {1} {2}'.format(year, month, day)
        date = datetime.datetime.strptime(date_str, '%Y %b %d')
        return {
            'title': title,
            'date': date,
            'url': link,
        }

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        html = html.encode('utf8', errors='ignore')
        image = pq(html)('#comic img').attr('src')
        if not image.startswith('http://'):
            image = 'http://' + image.strip('/')
        return {'image': image}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
