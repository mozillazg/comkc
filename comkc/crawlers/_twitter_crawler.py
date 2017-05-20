# -*- coding: utf-8 -*-
import asyncio
import logging
import sys

from comkc.crawlers import BaseWorker
from comkc.crawlers._twitter import get_user_medias

logger = logging.getLogger(__name__)


class TwitterWorker(BaseWorker):
    SCREEN_NAME = ''

    def __init__(self, n_tweets=100):
        super().__init__()
        self.n_tweets = n_tweets

    async def get_items(self):
        medias = await get_user_medias(
            self.config.peony_client, self.SCREEN_NAME,
            n_tweets=self.n_tweets
        )
        data = []

        for media in medias:
            data.append({
                'title': '{0}: {1}'.format(self.SITE, media.text),
                'url': media.origin_url,
                'image': media.media_url,
                'date': media.created_at,
            })
        return data

    async def parse_item(self, url):
        await asyncio.sleep(0)
        return {}


def main(worker_cls):
    n_tweets = 10
    if len(sys.argv) > 1:
        n_tweets = int(sys.argv[1])
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(worker_cls(n_tweets).run())
    finally:
        loop.close()
