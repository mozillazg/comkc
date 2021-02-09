# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'dinosaur | Twitter'
    BASE_URL = 'https://twitter.com/dinoman_j'
    ENABLE = True
    SCREEN_NAME = 'dinoman_j'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
