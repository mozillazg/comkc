# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'warandpeass | Twitter'
    BASE_URL = 'https://twitter.com/warandpeass'
    ENABLE = True
    SCREEN_NAME = 'warandpeass'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
