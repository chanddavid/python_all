import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://127.0.0.1:5501/mqtt") as websocket:
        # await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello())