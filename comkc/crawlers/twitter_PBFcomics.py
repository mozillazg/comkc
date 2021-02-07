# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Perry Bible Fellowship Comics | Twitter'
    BASE_URL = 'https://twitter.com/PBFcomics'
    ENABLE = True
    SCREEN_NAME = 'PBFcomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
