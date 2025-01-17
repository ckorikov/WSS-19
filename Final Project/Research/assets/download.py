from __future__ import absolute_import, print_function, unicode_literals

import asyncio
import functools
import io
import os
import zipfile
from itertools import islice
from urllib.parse import urlparse

import aiohttp
from github import Github

HERE = os.path.abspath(os.path.dirname(__file__))
timeout = aiohttp.ClientTimeout(total=10)


async def wait_all(args):
    return await asyncio.gather(*args)


def get_event_loop(loop=None):
    try:
        return loop or asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop


def run_in_loop(cor, loop=None):
    @functools.wraps(cor)
    def wrapped(*args, **kwargs):
        return get_event_loop(loop).run_until_complete(cor(*args, **kwargs))

    return wrapped


def list_split(iterable, n, reverse=False):
    """ Yield successive n-sized chunks from l. """

    if reverse:
        extra = len(iterable) % n
        if extra:
            yield tuple(iterable[0:extra])

        iterable = iterable[extra:]
    else:
        extra = 0

    iterable = iter(iterable)

    res = tuple(islice(iterable, n))
    while len(res) != 0:
        yield res
        res = tuple(islice(iterable, n))


async def download(session, url):
    path = os.path.join(
        HERE, "repos", "-".join(urlparse(url).path.split("/")[1:3]).replace("/", "-")
    )

    if os.path.exists(path):
        print("[exists]", url)
    else:
        try:
            async with session.get(url, timeout=timeout) as resp:
                print("downloading", url, "to", path)
                if resp.status == 200:
                    zip_buffer = io.BytesIO()
                    zip_buffer.write(await resp.read())
                    zip_buffer.seek(0)
                    with zipfile.ZipFile(zip_buffer, "r") as f:
                        f.extractall(path)
                        f.close()
        except asyncio.TimeoutError:
            print("[TIMEOUT]")
        except Exception:
            pass


async def downloadall(urls):
    async with aiohttp.ClientSession() as session:
        for batch in list_split(urls, 20):
            await wait_all(
                asyncio.create_task(download(session, url)) for url in batch
            )


def getrepourls(token: ""):
    if token:
        g = Github(token)
        repositories = g.search_repositories(query="language:Mathematica", sort="stars")

        for repo in repositories:
            yield "%s/archive/master.zip" % repo.clone_url[0:-4]
    else:
        print("Please, provide a GitHub API token")


@run_in_loop
async def main():
    await downloadall(getrepourls(""))


main()
