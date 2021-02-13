# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'ToothyBj Comic | Twitter'
    BASE_URL = 'https://twitter.com/toothybj'
    ENABLE = True
    SCREEN_NAME = 'toothybj'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
