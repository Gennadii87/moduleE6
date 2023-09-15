# Generated by Django 4.2.5 on 2023-09-14 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='group_avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('display_name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='chat.groupchat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.groupchat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='groupchat',
            name='members',
            field=models.ManyToManyField(related_name='group_chats', to='chat.userprofile'),
        ),
    ]