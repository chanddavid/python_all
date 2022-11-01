import asyncio
from time import sleep


async def func1():
    print("func 1")
    await asyncio.sleep(2)
    print("below func 1")

async def func2():
    print("func 2")
    await asyncio.sleep(1) 
    print("below 2")
    return "hello world" 

async def func3():
    print("func 3")
    await asyncio.sleep(3)
    print("below func 3")
    

async def main():
    for i in range(2):
        task1=asyncio.gather(func1(),func2(),func3())
        print(i)
        await asyncio.sleep(1)
        val=await task1
        print(val)

asyncio.run(main())


# import asyncio

# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({number}), currently i={i}...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#     return f

# async def main():
#     L = asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#     await asyncio.sleep(1)
#     print("hello")
#     await L
#     print(L)

# asyncio.run(main())






















