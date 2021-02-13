# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Skeleton Claw | Twitter'
    BASE_URL = 'https://twitter.com/skeleton_claw'
    ENABLE = True
    SCREEN_NAME = 'skeleton_claw'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
