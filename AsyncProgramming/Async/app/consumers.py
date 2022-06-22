import json
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from app.thrd import AsyncEmails

your_email = "tankmansodari.073@kathford.edu.np"
email_to = "tankamansodari7@gmail.com"
password = "sseccus@tankmans"
subject = "Freeze Temperature Report"
text = """\
    Hi,
    Your device temperature is getting Down.do something"""
textType="plain"
port=587

class SyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket is connected', event)
        await self.send({
            'type': 'websocket.accept'
        }
        )
    async def websocket_receive(self, event):
        print("data received from client", event)
        for i in range(10):
            if i == 7:
                task1= asyncio.create_task(AsyncEmails(your_email,
                                 [email_to],
                                 password,
                                 subject,
                                 text,
                                 textType,
                                 port).send_mail_async())
                print(task1)
                print("hello")
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": i})
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self, event):
        print('websocket Disconnect', event)
        raise StopConsumer()
