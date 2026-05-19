from django.db import models
from django.contrib.auth.models import User


# ---------------- PROFILE ----------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, blank=True, default='')
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_followers_count(self):
        return Follow.objects.filter(following=self.user).count()

    def get_following_count(self):
        return Follow.objects.filter(follower=self.user).count()

    def get_posts_count(self):
        return Post.objects.filter(user=self.user).count()


# ❌ REMOVE SIGNALS (IMPORTANT)
# We are NOT using post_save signals anymore
# because they cause "profile missing" bugs in dev projects


# ---------------- POST ----------------
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'


# ---------------- COMMENT ----------------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']


# ---------------- LIKE ----------------
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


# ---------------- FOLLOW ----------------
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')