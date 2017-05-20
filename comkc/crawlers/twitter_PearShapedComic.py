# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Pear-Shaped Comics | Twitter'
    BASE_URL = 'https://twitter.com/PearShapedComic'
    ENABLE = True
    SCREEN_NAME = 'PearShapedComic'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
