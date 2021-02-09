# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'impostor bear | Twitter'
    BASE_URL = 'https://twitter.com/impostorbear'
    ENABLE = True
    SCREEN_NAME = 'impostorbear'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
