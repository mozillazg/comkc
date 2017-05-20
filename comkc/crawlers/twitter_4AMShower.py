# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Guy Kopsombut | Twitter'
    BASE_URL = 'https://twitter.com/4AMShower'
    ENABLE = True
    SCREEN_NAME = '4AMShower'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
