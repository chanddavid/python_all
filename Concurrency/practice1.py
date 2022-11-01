import asyncio
from time import sleep


async def sum(a,b):
    print(a+b)
    await asyncio.sleep(1)
    print("add")
async def mult(a,b):
    print(a*b)
    await asyncio.sleep(1)
    print("sub")

async def loops(a,b):
    task1=asyncio.create_task(sum(a,b))
    task2=asyncio.create_task(mult(a,b))
    
    for i in range(1):
        print(i)
        await asyncio.sleep(1)
    print("main")

asyncio.run(loops(1,2))

