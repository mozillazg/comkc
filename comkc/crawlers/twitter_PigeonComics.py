# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'PigeonComics | Twitter'
    BASE_URL = 'https://twitter.com/PigeonComics'
    ENABLE = True
    SCREEN_NAME = 'PigeonComics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
