import json
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from random import randrange
from app.thrd import EmailThread

emailthread=EmailThread()

class SyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket is connected', event)
        await self.send({
            'type': 'websocket.accept'
        }
        )

    async def websocket_receive(self, event):
        print("data received from client", event)
        for i in range(25):
            if i==7:
                emailthread.start()
                print("its 7")
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": i})
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('websocket Disconnect', event)
        raise StopConsumer()
