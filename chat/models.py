from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    display_name = models.CharField(max_length=255)
    groups = models.ManyToManyField('GroupChat', related_name='user_groups', blank=True)

    def __str__(self):
        return self.display_name

class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='group_avatars/', blank=True, null=True)
    members = models.ManyToManyField(UserProfile, related_name='group_chats')

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.display_name}: {self.content}'
