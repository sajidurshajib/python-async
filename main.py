import time
import requests
import asyncio
import aiohttp


def main():
    s = sync_fetch(num=100)
    a = async_fetch(num=100)

    print("-"*10)
    print(f"Fetch as Sync time: {s}")
    print(f"Fetch as Async time: {a}")


def sync_fetch(num: int):
    # fetch as sync
    i = 1
    start_time = time.time()
    while i < num:
        data = sync_def(id=i)
        print(data)
        i += 1
    end_time = time.time()
    time_count = end_time-start_time
    return int(time_count)


def async_fetch(num: int):
    # fetch as async
    i = 1
    start_time = time.time()
    while i < num:
        data = asyncio.run(async_def(id=i))
        print(data)
        i += 1
    end_time = time.time()
    time_count = end_time-start_time
    return int(time_count)


def sync_def(id: int):
    data = requests.get(f'https://jsonplaceholder.typicode.com/photos/{str(id)}')
    return data.json()


async def async_def(id: int):
    async with aiohttp.ClientSession() as session:
        respoose = await session.get(f'https://jsonplaceholder.typicode.com/photos/{str(id)}')
        return await respoose.json()


if __name__ == '__main__':
    main()
