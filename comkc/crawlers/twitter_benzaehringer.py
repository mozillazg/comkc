# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Ben Zaehringer | Twitter'
    BASE_URL = 'https://twitter.com/benzaehringer'
    ENABLE = True
    SCREEN_NAME = 'benzaehringer'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
