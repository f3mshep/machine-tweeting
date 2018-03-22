import tweepy
import dotenv

def load_dot():

  dotenv.load()

def handleAuth():
  consumer_key = dotenv.get('ENV_KEY')
  consumer_secret = dotenv.get('ENV_SECRET')
  access_key = dotenv.get('TOKEN_KEY')
  access_secret = dotenv.get('TOKEN_SECRET')
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return auth

def handleAPI(auth):
  return tweepy.API(auth)

def authorizeApp():
  load_dot()
  auth = handleAuth()
  return handleAPI(auth)
