# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Jimmy Craig | Twitter'
    BASE_URL = 'https://twitter.com/jimmytried'
    ENABLE = True
    SCREEN_NAME = 'jimmytried'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
