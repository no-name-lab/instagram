from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follows', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.description}"


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return f"{self.user.username} likes {self.post.description}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, related_name='liked_comments', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment',)

    def __str__(self):
        return f"{self.user.username} likes {self.comment.text}"


class Story(models.Model):
    user = models.ForeignKey(UserProfile, related_name='stories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images/', blank=True, null=True)
    video = models.FileField(upload_to='story_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Save(models.Model):
    user = models.ForeignKey(UserProfile, related_name='saves', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class SaveItem(models.Model):
    post = models.ForeignKey(Post, related_name='save_items', on_delete=models.CASCADE)
    save = models.ForeignKey(Save, related_name='items', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.description} - {self.save.user.username}"


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
