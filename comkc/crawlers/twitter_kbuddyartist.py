# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'K | Twitter'
    BASE_URL = 'https://twitter.com/kbuddyartist'
    ENABLE = True
    SCREEN_NAME = 'kbuddyartist'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
