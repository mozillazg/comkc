# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Marko | Twitter'
    BASE_URL = 'https://twitter.com/MarkoRaassina'
    ENABLE = True
    SCREEN_NAME = 'MarkoRaassina'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
