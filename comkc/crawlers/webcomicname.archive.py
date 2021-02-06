# -*- coding: utf-8 -*-
import datetime
import logging
import re
from urllib.parse import urljoin

from pyquery import PyQuery as pq

from comkc.crawlers import BaseWorker

logger = logging.getLogger(__name__)


class Worker(BaseWorker):
    SITE = 'webcomic name'
    SITE_URL = 'https://webcomicname.com'
    # BASE_URL = 'https://webcomicname.com/page/1'
    BASE_URL = 'https://webcomicname.com'
    PAGE_URL = 'https://webcomicname.com/page/{page}'

    async def get_items(self):
        # html = await self.fetch_url(self.BASE_URL)
        pages = self._get_page_urls('')
        data = []
        for url in pages:
            html = await self.fetch_url(url)
            items = list(self._parse_page(html))
            data.extend(items)

        return data

    async def parse_item(self, url):
        return {}

    def _get_page_urls(self, html):
        max_page = 37
        return map(lambda p: self.PAGE_URL.format(page=p),
                   range(1, max_page + 1))

    def _parse_page(self, html):
        items = pq(html)('.container .main article')
        for item in items:
            item = pq(item)
            url = item('section.panel .date-note-wrapper a.post-date').attr('href')  # noqa
            title = url
            image = item('section.post .photo-wrapper img').attr('src')
            date = item('section.panel .date-note-wrapper a.post-date').text()
            date = date.strip()
            date = ' '.join(re.findall(r'(\S+) (\d+)[a-z]+, (\d+)', date)[0])

            yield {
                'title': '{0}: {1}'.format(self.SITE, title),
                'url': urljoin(self.SITE_URL, url),
                'date': datetime.datetime.strptime(date, '%b %d %Y'),
                'image': image,
            }


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Worker().run())
    finally:
        loop.close()
