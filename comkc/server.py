# -*- coding: utf-8 -*-
import datetime
import functools
import json
import os
import uuid

from aiohttp import web
from aiopg.sa import create_engine

from comkc import config, models

app = web.Application()
dsn = config.PG_DSN


def json_dump_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.ctime()
    if isinstance(obj, uuid.UUID):
        return obj.hex
    raise TypeError(obj)

json_dumps = functools.partial(json.dumps, default=json_dump_default, indent=2)
json_response = functools.partial(web.json_response, dumps=json_dumps)


def validate_uuid(uuid_str):
    try:
        value = uuid.UUID(uuid_str, version=4)
    except ValueError:
        return False
    return value.hex == uuid_str


async def list_comics(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            limit = 10
            offset = 0
            per_page = request.GET.get('per_page', '10')
            page = request.GET.get('page', '1')
            if per_page.isdigit() and int(per_page) > 0:
                if int(per_page) < config.MAX_LIMIT:
                    limit = int(per_page)
            if page.isdigit() and int(page) > 0:
                if int(page) < config.MAX_OFFSET:
                    offset = (int(page) - 1) * limit
                if offset > 0:
                    offset += 1

            random = request.GET.get('random')
            if random is not None:
                order_by = 'random()'
            else:
                order_by = models.table_comic.c.posted_at.desc()
            comics = await models.list_comics(
                conn, limit=limit, offset=offset, order_by=order_by
            )
            return json_response(comics)


async def get_comic(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            uuid = request.match_info['uuid']
            if not validate_uuid(uuid):
                return json_response({}, status=404)

            where = (models.table_comic.c.uuid == uuid)
            comic = await models.get_comic(conn, where)
            if comic is not None:
                return json_response(comic)
            else:
                return json_response({}, status=404)

app.router.add_route('GET', '/api/v1/comics/', list_comics)
app.router.add_route('GET', '/api/v1/comics/{uuid}', get_comic)

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    app.router.add_static('/', os.path.join(current_dir, '../frontend/'))
    web.run_app(app)
