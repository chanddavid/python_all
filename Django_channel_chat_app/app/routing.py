from django.urls import path
from .import consumers

websocket_urlpatterns=[
    path('ws/sc/<str:groupname>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/',consumers.MyASyncConsumer.as_asgi()),
]