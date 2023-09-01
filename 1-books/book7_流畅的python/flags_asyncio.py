import asyncio
import aiohttp # 1
from flags import BASE_URL, save_flag, show, main #2

@asyncio.coroutine #3
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url) #4
    image = yield from resp.read() #5
    return image

@asyncio.coroutine
def download_one(cc): #6
    image = yield from get_flag(cc) #7
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop() #8
    to_do = [download_one(cc) for cc in sorted(cc_list)] #9
    wait_coro = asyncio.wait(to_do) #10
    res, _ = loop.run_until_complete(wait_coro) #11
    loop.close() #12
    
    return len(res)


if __name__ == '__main__':
    main(download_many)