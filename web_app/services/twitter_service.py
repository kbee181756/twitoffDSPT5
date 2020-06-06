#web_app/services/twitter_service.py

import os
from pprint import pprint

from dotenv import load_dotenv
import tweepy

load_dotevn()

TWITTER_API_KEY = os.getenv("consumer_key")
TWITTER_API_SECRET = os.getenv("consumer_secret")
TWITTER_ACCESS_TOKEN = os.getenv("access_token")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("access_secret")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
print("AUTH", type(auth))
 
api = tweepy.API(auth)
print("API CLIENT", type(api))

# def twitter_api_client():
    return tweepy.API(auth)

if __name__ == "__main__":
    user  = api.get_user("username")
    print(type(user))
    pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)

    #tweets = api.user_timeline("username", tweet_mode='extended', count=150, exclude_replies=True, include_rts=False)
    tweets = api.user_timeline('username', tweet_mode='extneded', count=150)
    print(type(tweets))

    for tweet in tweets:
        print("-----")
        pritn(tweet.id, tweet.full_text)