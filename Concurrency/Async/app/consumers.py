# import json
# from time import sleep
# from channels.consumer import AsyncConsumer, SyncConsumer
# from channels.exceptions import StopConsumer
# import asyncio
# from app.thrds import AsyncEmails
# from app.env_vars import env


# class SyncConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print('websocket is connected', event)
#         await self.send({
#             'type': 'websocket.accept'
#         }
#         )
#     async def websocket_receive(self, event):
#         print("data received from client", event)
#         for i in range(10):
#             if i == 7:
#                 task1= asyncio.gather(AsyncEmails(env.your_email,
#                                  [env.email_to],
#                                  env.password,
#                                  env.subject,
#                                  env.text,
#                                  env.textType,
#                                  env.port).send_mail_async())
#                 print(task1)
#                 print("hello")
#             await self.send({
#                 'type': 'websocket.send',   
#                 'text': json.dumps({"count": i})
#             })
#             await asyncio.sleep(1)
#     async def websocket_disconnect(self, event):
#         print('websocket Disconnect', event)
#         raise StopConsumer()

import json
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from app.thrds import AsyncEmails
from app.env_vars import env
import requests


class SyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket is connected', event)
        await self.send({
            'type': 'websocket.accept'
        }
        )
    async def websocket_receive(self, event):
        print("data received from client", event)
        for i in range(2000):
            if i == 7:
                
                pass

                # r = requests.get(
                #         "http://api.sparrowsms.com/v2/sms/",
                #         params={'token' : 'v2_jAB7V9L3cl1Jay74q2nXM9IQgn0.3ea5',
                #             'from'  : 'Demo',
                #             'to'    : '9868559950',
                #             'text'  : 'SMS Message from Sparrow ho'})

                # status_code = r.status_code
                # response = r.text
                # response_json = r.json()
                # print(status_code)
                # print(response)
                # print(response_json)
                print("hello")
            await self.send({
                'type': 'websocket.send',   
                'text': json.dumps({"count": i})
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self, event):
        print('websocket Disconnect', event)
        raise StopConsumer()



