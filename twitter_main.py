import tweepy
from tweeter_creds import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#api will notify and wait if rate limits are exceeded
api=tweepy.API(auth)

tweets=api.home_timeline()
for tweet in tweets:
    print(tweet)

print(tweets)