from django.urls import path
from . import views

urlpatterns = [
    path('userprofiles/', views.UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('userprofiles/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail'),
    path('groupchats/', views.GroupChatListCreate.as_view(), name='groupchat-list-create'),
    path('groupchats/<int:pk>/', views.GroupChatDetail.as_view(), name='groupchat-detail'),
    path('messages/', views.MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message-detail'),
    path('groupchats/<int:chat_id>/members/', views.GroupChatMembersList.as_view(), name='groupchat-members-list'),
    path('chat/', views.chat_list, name='chat-list'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat-detail'),
]