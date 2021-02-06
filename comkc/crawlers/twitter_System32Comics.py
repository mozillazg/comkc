# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'System32Comics | Twitter'
    BASE_URL = 'https://twitter.com/System32Comics'
    ENABLE = True
    SCREEN_NAME = 'System32Comics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
