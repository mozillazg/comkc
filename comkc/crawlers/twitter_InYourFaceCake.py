# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'It me | Twitter'
    BASE_URL = 'https://twitter.com/InYourFaceCake'
    ENABLE = True
    SCREEN_NAME = 'InYourFaceCake'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
