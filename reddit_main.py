from reddit_creds import *
import praw

reddit = praw.Reddit(client_id=reddit_token,client_secret=reddit_secret,password=reddit_password,user_agent='redweeter-bot',username=reddit_user)

print(reddit.user.me())