# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Corgiyolk | Twitter'
    BASE_URL = 'https://twitter.com/corgiyolk'
    ENABLE = True
    SCREEN_NAME = 'corgiyolk'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
