from django.shortcuts import render
from rest_framework import generics, permissions
from .models import UserProfile, GroupChat, Message
from .serializers import UserProfileSerializer, GroupChatSerializer, MessageSerializer, GroupChatMembersSerializer

class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GroupChatListCreate(generics.ListCreateAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя как участника группового чата
        group_chat = serializer.save()
        group_chat.members.add(self.request.user.userprofile)

class GroupChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        # Проверяем, что текущий пользователь является отправителем сообщения
        if instance.user == self.request.user:
            instance.delete()
        else:
            # В случае, если пользователь не отправитель, можно вернуть ошибку
            raise PermissionDenied("You do not have permission to delete this message.")

class GroupChatMembersList(generics.ListAPIView):
    serializer_class = GroupChatMembersSerializer

    def get_queryset(self):
        # Получите групповой чат по его ID из URL
        chat_id = self.kwargs['chat_id']
        try:
            chat = GroupChat.objects.get(pk=chat_id)
            # Получите список участников этого чата
            return chat.members.all()
        except GroupChat.DoesNotExist:
            return UserProfile.objects.none()

def chat_list(request):
    chats = GroupChat.objects.all()
    return render(request, 'chat_list.html', {'chats': chats})

def chat_detail(request, chat_id):
    chat = GroupChat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=chat)
    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages})