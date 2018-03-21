import tweepy
import os
import pdb
import dotenv
import sys


dotenv.load()
CONSUMER_KEY = dotenv.get('ENV_KEY')
CONSUMER_SECRET = dotenv.get('ENV_SECRET')
ACCESS_TOKEN = dotenv.get('TOKEN_KEY')
TOKEN_SECRET = dotenv.get('TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('officialjaden')

pdb.set_trace()