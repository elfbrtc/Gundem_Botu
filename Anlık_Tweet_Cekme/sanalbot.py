# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:11:51 2020

@author: elifb
"""
#anlık tweetlerin elde edilmesi
import base64
import datetime

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
import time
import json

consumer_key="6jMugZKBt7xErar4B8JSzva1L"
consumer_secret="WbVUTZWEy8VsieKQ51OTufkI42ZKyDe9HjAjd3ypWavXqkRs5l"
access_key="947355630-mWbjgVid7aGlTYQewyTP73lmqWfaV2hvmRzvQatk"
access_secret="1RNVKzQiRMwCSzo7Yr6wKO0nJ206sNs4lZGtfoGZHMtjZ"




file = open(r"C:\Users\elifb\Desktop\projeler\SanalBot\corona5.txt",'a',encoding="utf-8")

class StreamListener(tweepy.StreamListener):
    
    batch_size=50
    tweets=[]
    tweet_batch_size=[]
    
 
    def on_status(self, status):
        
            
        #s1 = json.dumps(status)
        #tweet_data = json.loads(s1)
        tweet_data = json.dumps(status._json)
        tweet_data=json.loads(tweet_data)
        if "extended_tweet" in tweet_data:
            tweet = tweet_data['extended_tweet']['full_text']
            print(tweet)
            if 'RT' not in tweet:
                file.write(tweet+"\n")
                


if __name__=='__main__':


    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')

    tags = ["covid19","korona"]
    stream.filter(track=tags,languages = ["tr"])

#eski tweetlere ulşmak için bu kod eklenebilir
import GetOldTweets3 as got
text_query = '#covid19'
since_date = '2020-04-01'
until_date = '2021-01-10'
count = 10000
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query).setSince(since_date).setUntil(until_date).setMaxTweets(count).setLang('tr')
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]