# -*- coding: utf-8 -*-
import datetime
import functools
import json
import uuid

from aiohttp import web
from aiopg.sa import create_engine

from comkc import config
from comkc import models

app = web.Application()
dsn = config.PG_DSN


def json_dump_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.ctime()
    if isinstance(obj, uuid.UUID):
        return str(obj)
    raise TypeError(obj)


json_dumps = functools.partial(json.dumps, default=json_dump_default, indent=2)
json_response = functools.partial(web.json_response, dumps=json_dumps)


def validate_uuid(uuid_str):
    try:
        value = uuid.UUID('4516c3c7-528c-4b40-8778-dcdc1ee22ed0', version=4)
    except ValueError:
        return False
    return value.hex == uuid_str


async def hello(request):
        return web.Response(body=b"Hello, world")


async def list_comics(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            limit = 10
            offset = 0
            per_page = request.GET.get('per_page', '10')
            page = request.GET.get('page', '1')
            if per_page.isdigit() and int(per_page) > 0:
                limit = int(per_page)
            if page.isdigit() and int(page) > 0:
                offset = (int(page) - 1) * limit
                if offset > 0:
                    offset += 1

            comics = await models.list_comics(conn, limit=limit, offset=offset)
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
    web.run_app(app)
