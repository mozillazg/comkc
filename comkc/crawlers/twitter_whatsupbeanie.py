# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Beanie | Twitter'
    BASE_URL = 'https://twitter.com/whatsupbeanie'
    ENABLE = True
    SCREEN_NAME = 'whatsupbeanie'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
