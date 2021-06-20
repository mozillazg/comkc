# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Gudim | Twitter'
    BASE_URL = 'https://twitter.com/like_gudim'
    ENABLE = True
    SCREEN_NAME = 'like_gudim'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
