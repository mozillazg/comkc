# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'graphing my depression | Twitter'
    BASE_URL = 'https://twitter.com/depressedgraph'
    ENABLE = True
    SCREEN_NAME = 'depressedgraph'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
