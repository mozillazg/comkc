# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Alex Norris | Twitter'
    BASE_URL = 'https://twitter.com/dorrismccomics'
    ENABLE = True
    SCREEN_NAME = 'dorrismccomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)
