# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'dinosaur | Twitter'
    BASE_URL = 'https://twitter.com/dino_comics'
    ENABLE = True
    SCREEN_NAME = 'dino_comics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
