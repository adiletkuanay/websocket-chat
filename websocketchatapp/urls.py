from django.urls import path
from . import views
from . import consumers

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create-chat-room/', views.create_chat_room, name='create_chat_room'),
    path('chat-room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('logout/', views.logout_view, name='logout'),
    path('chat-room/<int:room_id>/delete/', views.delete_chat_room, name='delete_chat_room'),
]

websocket_urlpatterns = [
    path(r"ws/chat/(?P<room_id>\d+)/$", consumers.ChatConsumer.as_asgi()),
]