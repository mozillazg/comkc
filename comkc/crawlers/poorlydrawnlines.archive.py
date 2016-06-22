# -*- coding: utf-8 -*-
import datetime
import logging
import re

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'Poorly Drawn Lines'
    BASE_URL = 'http://poorlydrawnlines.com/archive/'
    ENABLE = False

    async def get_items(self):
        html = await self.fetch_url(self.BASE_URL)
        tags = pq(html)('.wrapper .page ul li a')
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
        image = pq(html)('.post p img').attr('src')
        resp = await self.fetch_url(image, method='head', return_resp=True)
        img_date_str = resp.headers['Last-Modified']
        img_date = datetime.datetime.strptime(
            img_date_str, '%a, %d %b %Y %H:%M:%S GMT'
        )
        url_match = re.search(
            r'/(?P<year>\d{4})/(?P<month>\d{2})/[^/]+$', image
        )
        try:
            url_date = datetime.datetime(
                int(url_match.group('year')), int(url_match.group('month')), 1
            )
        except AttributeError:
            date = img_date
        else:
            date = datetime.datetime(
                url_date.year, url_date.month, img_date.day,
                hour=img_date.hour, minute=img_date.minute,
                second=img_date.second
            )
        return {'image': image, 'date': date}

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
