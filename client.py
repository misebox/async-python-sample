import asyncio
import time
import aiohttp


async def get_request(session, no):
    response = await session.get(f'http://localhost:9999/{no}')
    content = await response.text()
    print(f"{time.strftime('%X')} - {response.status} {content}")
    return content

async def run():
    tasks = []
    print(f"{time.strftime('%X')} - Start")
    async with aiohttp.ClientSession() as session:
        for n in range(10):
            tasks.append(get_request(session, n))
        ret = await asyncio.gather(*tasks)
        print('ret', ret)
    print(f"{time.strftime('%X')} - Finish")


asyncio.run(run())
