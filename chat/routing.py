from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import YourConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/chat/", YourConsumer.as_asgi()),
    ]),
})