# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Sarah Andersen | Twitter'
    BASE_URL = 'https://twitter.com/SarahCAndersen'
    ENABLE = True
    SCREEN_NAME = 'SarahCAndersen'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
