import json
from time import sleep
import asyncio
from channels.consumer import SyncConsumer, AsyncConsumer 
from channels.exceptions import StopConsumer 
from asgiref.sync import async_to_sync  

class MySyncConsumer(SyncConsumer):     
    def websocket_connect(self, event):         
        print('websocket Connect', event) 
        print("channel layer.",self.channel_layer)
        print("channel name.",self.channel_name)
        self.groupname=self.scope['url_route']['kwargs']['groupname']
        #group.add is async method but we have sync consumer so convert this method into sync
        async_to_sync(self.channel_layer.group_add)(self.groupname,self.channel_name)

        self.send({             
            'type': 'websocket.accept' ,      
            }         
            )   
                
    def websocket_receive(self, event):        
            print("message received from client",event)  
            async_to_sync(self.channel_layer.group_send)(self.groupname,
            {
                'type':'chat.message',
                'message':event['text']
            })
    def chat_message(self,event):
        print('event',event)
        print('event',event['message'])
        self.send({
             'type': 'websocket.send',
             'text':event['message']
        })

    def websocket_disconnect(self, event):         
            print('websocket Disconnect', event)           
            async_to_sync(self.channel_layer.group_discard)(self.groupname,self.channel_name)
            raise StopConsumer()
    









class MyASyncConsumer(AsyncConsumer):     
    async def websocket_connect(self, event):         
        print("websocket Connect", event)  
  
    async def websocket_receive(self, event):         
        print("Message received from client",event['text']) 

    async def websocket_disconnect(self, event):         
        print("websocket Disconnect", event)