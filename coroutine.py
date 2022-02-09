import time
import asyncio



async def main():

    async def say_hello():
        await asyncio.sleep(1.5)
        print('hello')


    task = asyncio.create_task(say_hello())

    print('before asyncio.sleep 1', task.done())

    await asyncio.sleep(1)

    print('after asyncio.sleep 1', task.done())

    print('before asyncio.sleep 2', task.done())

    await asyncio.sleep(1)

    print('after asyncio.sleep 2', task.done())


    print('done', task.done())
    await task


asyncio.run(main())
