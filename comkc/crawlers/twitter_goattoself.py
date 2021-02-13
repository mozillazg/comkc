# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Goat to Self | Twitter'
    BASE_URL = 'https://twitter.com/goattoself'
    ENABLE = True
    SCREEN_NAME = 'goattoself'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
