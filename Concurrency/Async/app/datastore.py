import json
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from app.thrds import AsyncEmails
from app.env_vars import env



import pymongo
from datetime import datetime
conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.TEST

class SyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket is connected', event)
        
        await self.send({
            'type': 'websocket.accept'
        }       
        )
    async def websocket_receive(self, event):
        print("data received from client", event)
        
        A="dog"
        collections = db.list_collection_names()
        print(collections)
        list=[]
        if A not in  collections:
            print("False")
            db.create_collection(A, timeseries={
                    'timeField': "timestamp",
                    'metaField': "metadata",
                    'granularity': "seconds"
                })  
        print("True") 
        for i in range(15):
            list.append( {
                    "metadata": {"device_name": "freeze", "type": "temperature"},
                    "timestamp":datetime.today().replace(microsecond=0),
                    "temp": i
                })
            db[A].insert_many(list)  
            print(collections)
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": i})
            })
            await asyncio.sleep(1)          

    async def websocket_disconnect(self, event):
        print('websocket Disconnect', event)
        raise StopConsumer()
