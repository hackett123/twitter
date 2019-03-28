# Michael Hackett's Twitter for CIS 192

## Routes

### Splash : ""

Brief description of the site with links to log in or sign up. Also lists all registered users.

### Toggle Dark Mode : "/toggle_dark_mode"

Lets the user swap between a light theme and a dark theme, both of which are extensions of Bulma. All credit goes to Bulmaswitch for their designs (link in extra credit)

### Home : "/home"

User's homepage with links to their profile page or to log out. There are a list of recent tweets in most recent order, which features replies as well. There is a list of hashtags that are clickable. The user can post a tweet from the home page with the form above the existing tweets.

### Login : "/login"

This is the page where existing users can re-authenticate into our system to receive access to the main app.

### Like Tweet : "/like_tweet"

User can click the like button a tweet to like it. It will be added to their list of likes and will be displayed when a user visits their own profile page. The number of likes a tweet receives is visible on the tweet itself.

### Delete Tweet : "/delete_tweet"

User can delete their own tweets from their profile page if they decide they no longer like it. It will no longer be visible to any user.

### Delete Account : "/delete_account"

User can delete their account, accessible via the footer of their own profile page. This action cannot be undone and their presence on the site ends until they choose to make a new account.

### Profile : "/profile"

User can view either their own profile or another user's profile, each of which offer different views. On their own profile, a user can modify their bio, pic, delete their tweets,and see their likes and followers. If viewing another user, they can see their bio, pic, followers / following count, and tweets only (total number and content).

### Change Bio Description : "/change_bio"

User can change their description that other users see when they visit the user's profile.

### Change Profile Picture : "/change_pic"

User can change their profile picture. Do so by providing the image address.

### Establish Follow / Break Follow : "/establish_follow", "/break_follow"

User can follow or unfollow another user. Right now this actually creates a symmetric relationship, so followng someone means they follow you too. Friendship should be symmetric anyway! This friendship is reflected by either viewing your own profile and looking at your follower list and also in the following/follower count that everyone can see on your profile.

### Block User : "/block_user"

A user can permanently block another user by viewing their profile and scrolling down past their tweets and hitting the block button. This action cannot be undone. The consequence of blocking a user is that their content is no longer viewable when you are on the site. Other users can still see and interact with them.

### Hashtag : "/hashtag"

A tweet can include hashtags by putting text directly after the # character. These hashtags are parsed and put into a list that can be seen on the right side of the home page, and clicking on any of these hashtags will direct the user to a page which will display all tweets that have used that hashtag!

### Reply To Tweet : "/reply_to_tweet"

Each tweet can be responded to by any user! Replying to a tweet adds your reply to the already present list of replies or starts off the thread if it's the first one.

### Like Reply : "/like_reply"

Each tweet's replies can be liked by users. This lets a user like / unlike a reply. The number of likes a reply has is listed next to this button.

## Design Considerations

Our models are User, Tweet, Hashtag, Reply.

I wanted a splah page separate from login / signup, so I separated those three into their own routes. We have a user driven experience in mind, so each user's experience is individualized through theme, profile pic, bio, followers, likes, replies, etc, so accordingly every user creates their own account and can interact with other users in their own way.

## Collaborators

Jamie Tomlinson is my 192 collaborator, she's the best!

## Extra Credit

### Follower System

This is ~half~ implemented. As of right now my follower / following system is behaving like an undirected graph instead of a directed graph, so I'll try to fix this before my final submission, but as of right now following symmetric.

### Replying to Tweets

Users can reply to tweets on the home page! All replies to a tweet will be displayed on the tweet with the user, time, and content of the reply.

### Extending User Model

I extended the user model in order to gain some extra functionality, such as a bio annd a profile picture which are of course customizable. Other minor things are included as well, including number of tweets, the tweets they've liked, a way to remember blocked users, etc

### Blocking Users

For our Twitter, our motto is never look back! When you block a user, you'll never see them again on your account. Be careful!

### Additional Content

I've found some cool modifications on the Bulma framework at this opensource repo [Bulmaswitch](https://jenil.github.io/bulmaswatch/) and I've added the ability to toggle dark mode!

## How to Run

Just like any Django project, you can simply run from the commannd line with "python manage.py runserver" after installing the relevant dependencies listed in requirements.txt