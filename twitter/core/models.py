from django.db import models
from django.contrib.auth.models import AbstractUser

import os

# code for this method taken from stack overflow https://stackoverflow.com/questions/8189800/django-store-user-image-in-model
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

light_theme = "https://unpkg.com/bulmaswatch/cerulean/bulmaswatch.min.css"
dark_theme = "https://unpkg.com/bulmaswatch/darkly/bulmaswatch.min.css"

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    num_tweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    bio = models.TextField(default="Hi! This is my twitter!")
    profile_pic = models.CharField(max_length=200, default="https://bulma.io/images/placeholders/128x128.png")
    followers = models.ManyToManyField('self', related_name="followers")
    following = models.ManyToManyField('self', related_name="following")
    blocked_users = models.ManyToManyField('self', related_name="blocked_users")
    theme = models.CharField(max_length=256, default=light_theme)
    is_dark = models.BooleanField(default=False)


class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    num_usages = models.IntegerField(default=0)
    name = models.CharField(default="",max_length=256)

class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_author")
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name = "reply_liked_by")
    created_at = models.DateTimeField(auto_now=True)

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "author")
    created_at = models.DateTimeField(auto_now = True)
    hashtags = models.ManyToManyField(Hashtag)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name = "liked_by")
    replies = models.ManyToManyField(Reply, related_name="replies")


