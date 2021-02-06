# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Safely Endangered | Twitter'
    BASE_URL = 'https://twitter.com/EndangeredComic'
    ENABLE = True
    SCREEN_NAME = 'EndangeredComic'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
