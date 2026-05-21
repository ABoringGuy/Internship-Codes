import asyncio
import time

async def greet_after_delay(name):
    print(f"Starting {name}...")
    await asyncio.sleep(2)
    print(f"Hello, {name}!")

async def main():
    start = time.perf_counter()
    """These commented codes below are synchronous"""
    # t1=greet_after_delay("Alex")
    # t2=greet_after_delay("Bob")
    # t3=greet_after_delay("Charlie")

    t1=asyncio.create_task(greet_after_delay("Alex"))
    t2=asyncio.create_task(greet_after_delay("Bob"))
    t3=asyncio.create_task(greet_after_delay("Charlie"))
    await t1
    await t2
    await t3

    """We can execute all asynchronous calls like below. Comment above and use below to test"""
    # await asyncio.gather(greet_after_delay("Alex"),greet_after_delay("Bob"),greet_after_delay("Charlie"))

    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f} seconds")


asyncio.run(main())