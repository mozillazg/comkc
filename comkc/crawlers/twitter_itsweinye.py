# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'It is Weinye | Twitter'
    BASE_URL = 'https://twitter.com/itsweinye'
    ENABLE = True
    SCREEN_NAME = 'itsweinye'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
