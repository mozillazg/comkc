# -*- coding: utf-8 -*-
import asyncio
import glob
import logging
import os

from comkc import config
from comkc.crawlers import crawlers

logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.realpath(__file__))

for path in glob.glob(
            os.path.join(current_dir, 'crawlers') + os.path.sep + '*.py'
        ):
    if '__init__' in path:
        continue
    module = 'comkc.crawlers.{}'.format(os.path.basename(path).split('.')[0])
    __import__(module)


async def main(loop):
    futures = []
    for name, func in crawlers.items():
        logger.info('got an crawler: {}'.format(name))
        future = asyncio.ensure_future(func())
        futures.append(future)
    await asyncio.wait(futures)


if __name__ == '__main__':
    if config.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO
    format_str = '%(levelname)s %(asctime)s %(module)s %(name)s %(message)s'
    logging.basicConfig(level=level, format=format_str)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    except KeyboardInterrupt:
        loop._run_once()
        loop.stop()
    finally:
        loop.close()
