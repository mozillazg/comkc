# -*- coding: utf-8 -*-
import aiohttp
import logging

logger = logging.getLogger(__name__)
CLIENT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:84.0) Gecko/20100101 Firefox/84.0',  # noqa
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  # noqa
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


async def fetch_url(url, binary=False, return_resp=False, method='GET',
                    referer=None):
    headers = {}
    if referer:
        headers['Referer'] = referer
    headers.update(CLIENT_HEADERS)

    async with aiohttp.ClientSession(headers=CLIENT_HEADERS) as session:
        if referer:
            async with getattr(session, method.lower())(referer) as resp:
                await resp.read()

        logger.info('start fetch %s', url)
        async with getattr(session, method.lower())(url) as resp:
            resp.raise_for_status()
            if return_resp:
                return resp
            if binary:
                return await resp.read()
            else:
                return await resp.text()
