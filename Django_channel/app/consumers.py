import json
from time import sleep
import asyncio
from channels.consumer import SyncConsumer, AsyncConsumer  
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):     
    def websocket_connect(self, event):         
        print('websocket Connect', event)         
        self.send({             
            'type': 'websocket.accept'       
            }         
            )      
    # def websocket_receive(self, event):        
    #         print("message received from client",event['text']) 
    #         for i in range(10):
    #             self.send({
    #             'type':'websocket.send',
    #             'text':str(i)
    #         })    
    #             sleep(1) 
    def websocket_receive(self, event):        
            print("message received from client",event['text']) 
            for i in range(10):
                self.send({
                'type':'websocket.send',
                #text only take string 
                'text':json.dumps({"count":i})
            })    
                sleep(1)
    def websocket_disconnect(self, event):         
            print('websocket Disconnect', event)    
            raise StopConsumer()
    
class MyASyncConsumer(AsyncConsumer):     
    async def websocket_connect(self, event):         
        print("websocket Connect", event)  
        await self.send({
            'type':'websocket.accept'
        })    
    async def websocket_receive(self, event):         
        print("Message received from client",event['text']) 
        for i in range(10):
            await self.send({
            'type':'websocket.send',
            'text':str(i)
            })    
            await asyncio.sleep(1)  
    async def websocket_disconnect(self, event):         
        print("websocket Disconnect", event)