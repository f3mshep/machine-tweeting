#!/usr/bin/env python3
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv
import sys
from get_twitter_auth import authorizeApp

#Twitter API credentials



def get_all_tweets(screen_name):
	#authorize twitter, initialize tweepy

	api = authorizeApp()

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name=screen_name, count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(
			screen_name=screen_name, count=200, max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at,
               tweet.text] for tweet in alltweets]

	#write the csv
	with open('../data/%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id", "created_at", "text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
  	#pass in the username of the account you want to download
	if len(sys.argv) != 2:
		print("Wrong number of arguments")
		sys.exit(1)

	get_all_tweets(sys.argv[1])
	sys.exit(0)
