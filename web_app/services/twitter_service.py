#web_app/services/twitter_service.py


load_dotevn()

TWITTER_API_KEY = os.getenv("consumer_key")
TWITTER_API_SECRET = os.getenv("consumer_secret")
TWITTER_ACCESS_TOKEN = os.getenv("access_token")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("access_secret")


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
print("AUTH", type(auth))
 
api = tweepy.API(auth)
print("API CLIENT", type(api))


user  = api.get_user("username")
print(type(user))