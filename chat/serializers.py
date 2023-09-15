from rest_framework import serializers
from .models import UserProfile, GroupChat, Message

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'avatar', 'display_name', 'groups')

class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = ('name', 'avatar')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'content', 'timestamp', 'chat')

class GroupChatMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'avatar', 'display_name', 'groups')
