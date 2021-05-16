# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Weng Chen | Twitter'
    BASE_URL = 'https://twitter.com/messycow'
    ENABLE = True
    SCREEN_NAME = 'messycow'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
