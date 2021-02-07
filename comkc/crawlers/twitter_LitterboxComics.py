# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Litterbox Comics | Twitter'
    BASE_URL = 'https://twitter.com/LitterboxComics'
    ENABLE = True
    SCREEN_NAME = 'LitterboxComics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
