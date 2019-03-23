from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    num_tweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    bio = models.TextField(default="Hi! This is my twitter!")


class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    num_usages = models.IntegerField(default=0)
    name = models.CharField(default="",max_length=256)

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    hashtags = models.ManyToManyField(Hashtag)
    likes = models.IntegerField(default=0)
    #liked_by = models.ManyToManyField(User)


