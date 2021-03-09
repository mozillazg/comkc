# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'the Awkward Yeti (Nick Seluk) | Twitter'
    BASE_URL = 'https://twitter.com/theawkwardyeti'
    ENABLE = True
    SCREEN_NAME = 'theawkwardyeti'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
