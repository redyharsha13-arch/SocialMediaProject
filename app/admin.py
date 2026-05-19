from django.contrib import admin
from .models import Profile, Post, Comment, Like, Follow


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    search_fields = ['user__username']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['user__username', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'timestamp']
    search_fields = ['user__username', 'text']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'timestamp']


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following', 'timestamp']
