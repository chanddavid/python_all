
from django.urls import path

from . import datastore
from .import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.SyncConsumer.as_asgi()),
    # path('ws/sc/',datastore.SyncConsumer.as_asgi()),
    path('ws/ac/',consumers.AsyncConsumer.as_asgi())
]






# _instance = None

#     @staticmethod
#     def getInstance():
#         """ static access method. """
#         if SyncConsumer._instance == None:
#             SyncConsumer()
#         return SyncConsumer._instance

#     def __init__(self):
#         """ virtually private constructor. """
#         if SyncConsumer._instance != None:
#             raise Exception(" This MQTTProtocolConfig class is a Singleton !")
#         else:
#             self.your_email = env.your_email
#             self.email_to = env.email_to
#             self.password = env.password
#             self.subject = env.subject
#             self.text = env.text
#             self.textType = env.textType
#             self.port = env.port

#             SyncConsumer._instance = self
