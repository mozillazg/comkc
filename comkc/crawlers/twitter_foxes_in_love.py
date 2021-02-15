# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Foxes in Love | Twitter'
    BASE_URL = 'https://twitter.com/foxes_in_love'
    ENABLE = True
    SCREEN_NAME = 'foxes_in_love'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
