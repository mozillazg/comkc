# -*- coding: utf-8 -*-
import logging
import os

PG_DSN = os.environ['COMKC_PG_DSN']
DEBUG = (os.getenv('COMKC_DEBUG') == 'true')

QINIU = {
    'access_key': os.environ['COMKC_QINIU_ACCESS_KEY'],
    'secret_key': os.environ['COMKC_QINIU_SECRET_KEY'],
    'bucket_name': os.environ['COMKC_QINIU_BUCKET_NAME'],
    'url_format': os.environ['COMKC_QINIU_URL_FORMAT'],
}

WORKER_SLEEP = 60 * 60 * 8

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.INFO
format_str = '%(levelname)s %(asctime)s %(module)s %(name)s %(message)s'
logging.basicConfig(level=level, format=format_str)
