import tweepy
import os
import pdb
import dotenv
import sys
import re
import csv

#authorize twitter, initialize tweepy
dotenv.load()
CONSUMER_KEY = dotenv.get('ENV_KEY')
CONSUMER_SECRET = dotenv.get('ENV_SECRET')
ACCESS_TOKEN = dotenv.get('TOKEN_KEY')
TOKEN_SECRET = dotenv.get('TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)
screen_name = 'officialjaden'
#initialize a list to hold all the tweepy Tweets
alltweets = []

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(
	screen_name=screen_name, count=200, tweet_mode="extended")

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
	print ("getting tweets before %s" % (oldest))

	#all subsiquent requests use the max_id param to prevent duplicates
	new_tweets = api.user_timeline(
		screen_name=screen_name, count=200, max_id=oldest, tweet_mode="extended")

	#save most recent tweets
	alltweets.extend(new_tweets)

	#update the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	print ("...%s tweets downloaded so far" % (len(alltweets)))
cleaned_text = [re.sub(r'http[s]?:\/\/.*[\W]*', '', i.full_text, flags=re.MULTILINE) for i in alltweets] # remove urls
# cleaned_text = [re.sub(r'@[\w]*', '', i, flags=re.MULTILINE) for i in cleaned_text] # remove the @twitter mentions
# cleaned_text = [re.sub(r'RT.*','', i, flags=re.MULTILINE) for i in cleaned_text] # delete the retweets
#transform the tweepy tweets into a 2D array that will populate the csv
outtweets = [[tweet.id_str, tweet.created_at, cleaned_text[idx]] for idx,tweet in enumerate(alltweets)]

#write the csv
with open('%s_tweets.csv' % screen_name, 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at","text"])
	writer.writerows(outtweets)

pass
