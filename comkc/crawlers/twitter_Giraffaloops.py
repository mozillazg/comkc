# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'giraffalope | Twitter'
    BASE_URL = 'https://twitter.com/Giraffaloops'
    ENABLE = True
    SCREEN_NAME = 'Giraffaloops'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
