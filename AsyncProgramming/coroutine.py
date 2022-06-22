import asyncio
import time
async def say_something (delay, words):
    print (f"Before {words}")
    await asyncio.sleep(delay) 
    print (f"After {words}")
async def main():
    print (f"Started: {time.strftime('%X')}")
    task1= asyncio.create_task (say_something (1, "Task 1"))
    task2= asyncio.create_task(say_something (2, "Task 2"))
    
    await task1
    await task2
    print (f"Finished: {time.strftime('%X')}")
asyncio.run(main())
