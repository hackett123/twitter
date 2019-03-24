from django.shortcuts import render, redirect

'''These imports are standard features that Django gives us'''
from django.contrib.auth import authenticate, login, logout
from core.models import Tweet, User, Hashtag

# this import is for parsing for hashtags, used stack overflow to find the syntax.
import re



# Create your views here.
def splash(request):
    users = User.objects.all()
    return render(request, "splash.html", {"users":users})

def home(request):
    full_hashtag_set = set()
    post_hashtag_set = set()
    for tweet in Tweet.objects.all():
        for hashtag in tweet.hashtags.all():
            if hashtag not in full_hashtag_set:
                full_hashtag_set.add(hashtag)
    existing_tweets = Tweet.objects.all()
    if request.method == "POST":
        content = request.POST.get("content")
        hashtags = re.findall(r"#(\w+)", content)
        if len(hashtags) > 0:
            for w in hashtags:
                found = False
                for tweet in existing_tweets:
                    for hashtag in tweet.hashtags.all():
                        if w == hashtag.name and not found:
                            post_hashtag_set.add(hashtag)
                            found = True
                if not found:
                    post_hashtag_set.add(Hashtag.objects.create(name=w))
        author = request.user
        author.num_tweets += 1
        author.save()
        tweet = Tweet.objects.create(content=content, author=author)
        tweet.hashtags.set(post_hashtag_set)
        return redirect("/home")
    if request.user.is_authenticated:
        tweets = Tweet.objects.all()
        user = request.user
        return render(request, "home.html", {"tweets":tweets[::-1], "user":user, "hashtags":full_hashtag_set})
    else :
        redirect("/")

def login_(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            login(request, user)
            return redirect("/home")
    return render(request, "login.html", {})

def logout_(request):
    logout(request)
    return redirect("/")

def signup_(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        login(request, user)
        return redirect('/home')
    return render(request, 'signup.html', {})

def like_tweet(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    user = request.user
    if user not in tweet.liked_by.all():
        tweet.liked_by.add(user)
        tweet.likes += 1
        tweet.save()
    else :
        tweet.liked_by.remove(user)
        tweet.likes -= 1
        tweet.save()
    return redirect("/home")

def delete_tweet(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    author = tweet.author
    author.num_tweets -= 1
    author.save()
    tweet.delete()
    return redirect("/home")

def delete_account(request):
    user = User.objects.get(id=request.GET['id'])
    user.delete()
    return redirect("/")

def profile(request):
    if request.user.is_authenticated:
        curr_user = request.user
        requested_user = User.objects.get(id=request.GET['id'])
        tweets = Tweet.objects.all()
        return render(request, 'profile.html', {"tweets":tweets[::-1], "curr_user":curr_user, "requested_user":requested_user})
    return redirect("/")

def change_bio(request):
    if request.method == "POST":
        user = request.user
        user.bio = request.POST["bio"]
        user.save()
    return redirect("/home")

def change_pic(request):
    if request.method == "POST":
        user = request.user
        user.profile_pic = request.POST["pic"]
        user.save()
    return redirect("/home")


def hashtag(request):
    hashtag = Hashtag.objects.get(id=request.GET['id'])
    tweets = Tweet.objects.all()
    tweets_used = list()
    for tweet in tweets:
        if (hashtag in tweet.hashtags.all()):
            tweets_used.append(tweet)
    return render(request, "hashtag.html", {"hashtag":hashtag, "tweets_used":tweets_used[::-1]})

