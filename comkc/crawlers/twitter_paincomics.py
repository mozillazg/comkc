# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'constant pain | Twitter'
    BASE_URL = 'https://twitter.com/paincomics'
    ENABLE = False
    SCREEN_NAME = 'paincomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
