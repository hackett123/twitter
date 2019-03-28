"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import login_, logout_, signup_, delete_tweet, home, splash, delete_account, like_tweet, profile, hashtag, change_bio, change_pic, establish_follow, break_follow, block_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", splash, name="splash"),
    path("login", login_, name="login"),
    path("signup", signup_, name="signup"),
    path("logout", logout_, name="logout"),
    path("like_tweet", like_tweet, name="like_tweet"),
    path("delete", delete_tweet, name="delete"),
    path("delete_account", delete_account, name="delete_account"),
    path("home", home, name="home"),
    path("profile", profile, name="profile"),
    path("change_bio", change_bio, name="change_bio"),
    path("change_pic", change_pic, name="change_pic"),
    path("hashtag", hashtag, name="hashtag"),
    path("establish_follow", establish_follow, name="establish_follow"),
    path("break_follow", break_follow, name="break_follow"),
    path("block_user", block_user, name="block_user")

]
