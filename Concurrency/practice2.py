import asyncio

# import time

# async def say_after(delay, what):
#     print("tanka")
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))

#     task2 = asyncio.create_task(
#         say_after(2, 'world'))

#     print(f"started at {time.strftime('%X')}")

#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
background_tasks = set()

async def some_coro():
    print("hewlloi")

    

async def main():
    for i in range(2):
        task = asyncio.create_task(some_coro())

          # Add task to the set. This creates a strong reference.
        background_tasks.add(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)

asyncio.run(main())
