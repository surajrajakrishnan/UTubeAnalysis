# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:34:24 2019

@author: NDH00360
"""

import twitter
from twitter import Twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='kac8eSmENBLflIfVzWf8EJjAh',
                        consumer_secret='GlLn3dP7mpr3FsKq7RFmyHpd8hSJFyCxZgG5M2wG9A2bCpCDca',
                        access_token_key='596441322-R3D38tVOgZP6NMKTP0hApt4IoNdVLcLTEbEGIsUs',
                        access_token_secret='CX1DuODodjUVLwsTGsx9WvktB6TCwWeRKBNMOZd0BNCXt')


from twitter import *

t = Twitter(
    auth=OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret))


from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.oauth import OAuth
auth=OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        print (msg['direct_message']['text'])






    # These arguments are optional:
    stream_args = dict(
        timeout=args.timeout,
        block=not args.no_block,
        heartbeat_timeout=args.heartbeat_timeout)

    query_args = dict()
    if args.track_keywords:
        query_args['track'] = args.track_keywords

    stream = TwitterStream(auth=auth)
    if args.track_keywords:
        tweet_iter = stream.statuses.filter(**query_args)
    else:
        tweet_iter = stream.statuses.sample()

    # Iterate over the sample stream.
    for tweet in tweet_iter:
        # You must test that your tweet has text. It might be a delete
        # or data message.
        if tweet is None:
            printNicely("-- None --")
        elif tweet is Timeout:
            printNicely("-- Timeout --")
        elif tweet is HeartbeatTimeout:
            printNicely("-- Heartbeat Timeout --")
        elif tweet is Hangup:
            printNicely("-- Hangup --")
        elif tweet.get('text'):
            printNicely(tweet['text'])
        else:
            printNicely("-- Some data: " + str(tweet))







# test authentication
print(auth.VerifyCredentials())

# ------------------------------------------------------------------------

def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None
    
# ------------------------------------------------------------------------

search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])

# ------------------------------------------------------------------------

def buildTrainingSet(corpusFile, tweetDataFile):
    import csv
    import time 

    corpus=[]
    
    with open(corpusFile,'rb') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            corpus.append({"tweet_id":row[2], "label":row[1], "topic":row[0]})
    
    rate_limit=180
    sleep_time=900/180
    
    trainingDataSet=[]

    for tweet in corpus:
        try:
            status = twitter_api.GetStatus(tweet["tweet_id"])
            print("Tweet fetched" + status.text)
            tweet["text"] = status.text
            trainingDataSet.append(tweet)
            time.sleep(sleep_time)
        except: 
            continue
    # Now we write them to the empty CSV file
    with open(tweetDataFile,'wb') as csvfile:
        linewriter=csv.writer(csvfile,delimiter=',',quotechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"],tweet["text"],tweet["label"],tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet

# ------------------------------------------------------------------------

corpusFile = "YOUR_FILE_PATH/corpus.csv"
tweetDataFile = "YOUR_FILE_PATH/tweetDataFile.csv"

trainingData = buildTrainingSet(corpusFile, tweetDataFile)

# ------------------------------------------------------------------------

import re
from nltk.tokenize import word_tokenize
from string import punctuation 
from nltk.corpus import stopwords 

class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER','URL'])
        
    def processTweets(self, list_of_tweets):
        processedTweets=[]
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet["text"]),tweet["label"]))
        return processedTweets
    
    def _processTweet(self, tweet):
        tweet = tweet.lower() # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        tweet = word_tokenize(tweet) # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]
    
tweetProcessor = PreProcessTweets()
preprocessedTrainingSet = tweetProcessor.processTweets(trainingData)
preprocessedTestSet = tweetProcessor.processTweets(testDataSet)

# ------------------------------------------------------------------------

import nltk 

def buildVocabulary(preprocessedTrainingData):
    all_words = []
    
    for (words, sentiment) in preprocessedTrainingData:
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()
    
    return word_features

# ------------------------------------------------------------------------

def extract_features(tweet):
    tweet_words=set(tweet)
    features={}
    for word in word_features:
        features['contains(%s)' % word]=(word in tweet_words)
    return features 

# ------------------------------------------------------------------------

# Now we can extract the features and train the classifier 
word_features = buildVocabulary(preprocessedTrainingSet)
trainingFeatures=nltk.classify.apply_features(extract_features,preprocessedTrainingSet)

# ------------------------------------------------------------------------

NBayesClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures)

# ------------------------------------------------------------------------

NBResultLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in preprocessedTestSet]

# ------------------------------------------------------------------------

# get the majority vote
if NBResultLabels.count('positive') > NBResultLabels.count('negative'):
    print("Overall Positive Sentiment")
    print("Positive Sentiment Percentage = " + str(100*NBResultLabels.count('positive')/len(NBResultLabels)) + "%")
else: 
    print("Overall Negative Sentiment")
    print("Negative Sentiment Percentage = " + str(100*NBResultLabels.count('negative')/len(NBResultLabels)) + "%")
