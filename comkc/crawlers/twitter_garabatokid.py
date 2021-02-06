# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Garabato Kid | Twitter'
    BASE_URL = 'https://twitter.com/garabatokid'
    ENABLE = True
    SCREEN_NAME = 'garabatokid'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
