# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Enzo | Twitter'
    BASE_URL = 'https://twitter.com/enzocomics'
    ENABLE = True
    SCREEN_NAME = 'enzocomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
