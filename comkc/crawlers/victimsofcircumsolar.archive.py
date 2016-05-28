# -*- coding: utf-8 -*-
import datetime
import logging

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Victims of Circumsolar'
    BASE_URL = 'http://www.victimsofcircumsolar.com/archives/'
    ENABLE = False

    async def _get_one_year(self, url, year):
        html = await self.fetch_url(url)
        data = []
        for item in pq(html)('.month-table')('tr'):
            item = pq(item)
            date_str = '{0} {1}'.format(
                item('.archive-date').text().strip(), year
            )
            date = datetime.datetime.strptime(date_str, '%b %d %Y')
            title = item('a').text().strip()
            url = item('a').attr('href')
            data.append({
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': url,
                'date': date,
            })
        return data

    async def get_items(self):
        data = []
        for year in range(datetime.datetime.now().year, 2013 - 1, -1):
            url = self.BASE_URL + '?archive_year={0}'.format(year)
            year_data = await self._get_one_year(url, year)
            data.extend(year_data)
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
