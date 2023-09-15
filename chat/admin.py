from django.contrib import admin
from .models import UserProfile, GroupChat, Message
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'get_email')  # Добавили 'get_email'
    list_filter = ('user',)

    def get_email(self, obj):
        return obj.user.email  # Получаем адрес электронной почты пользователя

    get_email.short_description = 'Email'  # Описание поля в админке

@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('members',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp', 'chat')
    list_filter = ('user', 'chat')