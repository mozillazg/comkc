# -*- coding: utf-8
import asyncio
import logging

from aiopg.sa import create_engine
import qiniu

from comkc import config, models
from comkc.utils import fetch_url

dsn = config.PG_DSN
logger = logging.getLogger(__name__)


def upload(data, comic, params=None,
           mime_type='application/octet-stream',
           check_crc=False, *args, **kwargs):
    qn = qiniu.Auth(config.QINIU['access_key'], config.QINIU['secret_key'])
    token = qn.upload_token(config.QINIU['bucket_name'])
    filename = 'comkc/{}'.format(str(comic['uuid'].hex))
    ret, _ = qiniu.put_data(
        token, filename, data, params=params,
        mime_type=mime_type, check_crc=check_crc, *args, **kwargs
    )
    return config.QINIU['url_format'].format(filename=ret['key'])


async def upload_images():
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            comics = await models.list_comics(
                conn, (models.table_comic.c.cdn == ''),
                limit=1000
            )
            for comic in comics:
                image_url = comic['image']
                try:
                    image_data = await fetch_url(image_url, binary=True)
                    assert image_data
                except Exception as e:
                    logger.exception('download %s failed! \n%s', image_url, e)
                    continue
                try:
                    # 这里会阻塞 IO, 所以这个程序其实并不是一个异步的程序
                    cdn_url = upload(image_data, comic)
                except Exception as e:
                    logger.exception('upload %s failed! \n%s', image_url, e)
                    continue

                uuid = str(comic['uuid'])
                await models.update_comics(
                    conn, (models.table_comic.c.uuid == uuid), cdn=cdn_url
                )
                logger.info('download %s then upload to %s success!',
                            image_url, cdn_url)
                await asyncio.sleep(60 * 1)


async def main(loop):
    while True:
        await upload_images()
        await asyncio.sleep(60 * 60 * 8)


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
