# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Dami Lee | Twitter'
    BASE_URL = 'https://twitter.com/dami_lee'
    ENABLE = True
    SCREEN_NAME = 'dami_lee'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
