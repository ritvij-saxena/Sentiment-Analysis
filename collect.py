"""Collect Data"""

import os
from TwitterAPI import TwitterAPI
import re
import datetime
import time
import sys
import pickle

consumer_key = 'ARhDeefKMSvpabPc8oZVhMzAY'
consumer_secret = 'Cl8qluG2TPzpAM5tsRA29Imu7k7ZUifQvYhxNgeFI2cxvUhvmr'
access_token = '1089314726117625857-LzzDIqy4icWsjkTr8GWGSg08QOevmt'
access_token_secret = 'kfF8kHTPW8MRq69XdyHPDCzB3y1Eovm0E7sT5K8zQcO5o'

def get_twitter():
    return TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

def robust_request(twitter, resource, params, max_tries=5):
    for i in range(max_tries):
        request = twitter.request(resource, params)
        if request.status_code == 200:
            return request
        else:
            print('Got error %s \nsleeping for 15 minutes.' % request.text)
            sys.stderr.flush()
            time.sleep(61 * 15)

def collect_tweets(twitter,keywords):
    tweets_data=[]
    for i in range (0,10):
        time_param=datetime.datetime.now()-datetime.timedelta(days=i)
        time_param=time_param.strftime('%Y-%m-%d')
        request = robust_request(twitter,'search/tweets', {'q':keywords,'count':1000,'until':time_param,'lang':'en'})
        for r in request:
            tweets_data.append(r)
    tweets_text = [t for t in tweets_data if 'text' in t]
    writeToFile('raw_tweets.pkl',tweets_text)
    return tweets_text

def writeToFile(filename,list_friends):
    f = open(filename,'wb')
    pickle.dump(list_friends,f)
    f.close()
    
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def save_screen_names(tweets):
    f = open("ids.pkl", 'wb')
    ids = [tweet['user']['id'] for tweet in tweets]
    pickle.dump(ids,f)
    f.close()
    return

def save_tweets(tweets):
    f = open("tweets_text.pkl", 'wb')
    tokens = []
    for tweet in tweets:
        tokens.append(clean_tweet(tweet['text']))
    pickle.dump(tokens,f)
    f.close()
    return

def read_ids(filename):
    my_file = pickle.load(open(filename, "rb"))
    return my_file

def get_friends(twitter, ID):
    ids=[]
    request = robust_request(twitter, 'friends/ids', {'user_id': ID, 'count':500}, 1000)
    ids = [item for item in request]
    ids.sort(key = int)
    return ids

def main():
    print("Connecting to Twitter....")
    twitter = get_twitter()
    print("Connection established")
    
    print("Collecting tweets")
    keywords = "#AvengersEndgame OR Avengers Endgame OR MarvelStudios  -filter:retweets"
    tweets = collect_tweets(twitter,keywords)
    print("Clearing tweets for future use")
    save_tweets(tweets)
    save_screen_names(tweets)
    print("Get Ids")
    ids = read_ids('ids.pkl')
    friends = []
    for i in range(0, 5):
        friends.append(get_friends(twitter, ids[i]))
    print("Writing list to file")
    writeToFile('friends.pkl',friends)
    print("finished")


if __name__ == '__main__':
    main()