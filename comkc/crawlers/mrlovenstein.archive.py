# -*- coding: utf-8 -*-
import datetime
import logging
import re
from urllib.parse import urljoin

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Mr. Lovenstein'
    SITE_URL = 'http://www.mrlovenstein.com'
    BASE_URL = 'http://www.mrlovenstein.com/archive/page1'
    PAGE_URL = 'http://www.mrlovenstein.com/archive/page{page}'
    re_date = re.compile(r'Posted (.*) at')
    re_date_split = re.compile(r'[, ]+')

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        pages = self._get_page_urls(html)
        data = []
        for url in pages:
            html = await self.fetch_url(url)
            items = list(self._parse_page(html))
            data.extend(items)

        return data

    async def parse_item(self, url):
        html = await self.fetch_url(url)
        image = pq(html)('#comic_main_image').attr('src')
        if not image.startswith('http'):
            image = urljoin(self.SITE_URL, image)
        return {'image': image}

    def _get_page_urls(self, html):
        page_url = pq(html)('.page_nav li a')[-1].get('href')
        max_page = int(page_url[-2:])
        return map(lambda p: self.PAGE_URL.format(page=p),
                   range(1, max_page + 1))

    def _parse_page(self, html):
        items = pq(html)('.archive_list')
        for item in items:
            title_pq = pq(item)('.comic_title a')
            title = title_pq.text().strip(' .')
            url = title_pq.attr('href')
            date = self.re_date.findall(pq(item)('.comic_date').text())
            try:
                month, day, year = self.re_date_split.split(date[0])
            except ValueError as e:
                logger.exception(e)
                continue
            date = '{0} {1:0>2} {2}'.format(month, day, year)

            yield {
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': urljoin(self.SITE_URL, url),
                'date': datetime.datetime.strptime(date, '%B %d %Y'),
            }

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
