# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:00:07 2019

@author: NDH00360
"""

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import collections
from textblob import TextBlob
    #import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
    #from wordcloud import WordCloud, STOPWORDS
    #import matplotlib.pyplot as plt
    #stopwords = set(STOPWORDS)
#stopwords.update(["comprisi","module","Communication","head","sy","implem","enclosur","Vehicle","device","claim","mounted","apparatus", "video","NaN","claimed",'filed',"Technical Filed '",'disclosure',"invention","system","systems","method","includes" ,"methods", "present", "including", "poor","Cars","review"])
    

import os
import glob

os.chdir(r"C:\Users\NDH00360\Desktop\Normalization\compitetor")
result = [i for i in glob.glob('*.{}'.format("csv"))]
print(result)


for pathword in result:    
    dfcloud=pd.DataFrame()
    print(pathword)
    dfcloud=pd.read_csv(r"C:\Users\NDH00360\Desktop\Normalization\Compitetor\{}".format(pathword))
    
    textcloud=dfcloud['abstract']
    #print(type(textcloud))
    
    #textcloudstring="".join(textcloud)
    textcloudstring = ','.join(str(v) for v in textcloud)
    #pd.DataFrame.to_string(textcloud)
    print(textcloudstring)
    
    #import matplotlib.pyplot as plt
    
    #from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    stopwords = set(STOPWORDS)
    stopwords.update(["comprisi","head","sy","implem","enclosur","Vehicle","device","claim","mounted","apparatus", "video","NaN","claimed",'filed',"Technical Filed '",'disclosure',"invention","system","systems","method","includes" ,"methods", "present", "including", "poor","Cars","review"])
    
    
    from rake_nltk import Metric, Rake
    r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
   # r = Rake(ranking_metric=Metric.WORD_DEGREE)
    #r = Rake(ranking_metric=Metric.WORD_FREQUENCY)
    
    r=Rake(min_length=1, max_length=2)
    #print(textcloudstring)
    r.extract_keywords_from_text(textcloudstring)
    text=r.get_ranked_phrases()
    print(text)
    
    text50=text[:99]
    # Generate a word cloud image
    print(type(text50))
    
    
#    text50="".join(text50)
 #   print(text50)
    
    
    
    
    
    
    
    #def show_wordcloud(data,path):
    #    wordcloud = WordCloud(
    #        background_color='white',
    #        stopwords=stopwords,
    #        max_words=200,
    #        max_font_size=40, 
    #        scale=3,
    #        random_state=1 # chosen at random by flipping a coin; it was heads
    #    ).generate(str(data))
    #
    #    fig = plt.figure(1, figsize=(12, 12))
    #    plt.axis('off')
    #    title=path
    #    if title: 
    #        fig.suptitle(path, fontsize=20)
    #        fig.subplots_adjust(top=2.3)
    #    plt.savefig(path)
    #    plt.imshow(wordcloud)
    #    plt.show()
    #    
#    def generate_wc_data(text):
#        #pos_words = []
#        #neg_words = []
#        allwords = []
#        blob = TextBlob(text)
#        for sentence in blob.sentences:
#            value = sentence.sentiment.polarity
#            if value>=-1 and value<=1:
#                allwords.extend(sentence.split(" "))
#        #pos_words = [w for w in pos_words if not w.lower() in stop_words]
#        allwords = [w for w in allwords if not w.lower() in stop_words]
#        #neu_words = [w for w in neu_words if not w.lower() in stop_words]
#        #pos_words_dict = generate_freq(pos_words)
#        allwords_dict = generate_freq(allwords)
#        #neu_words_dict = generate_freq(neu_words)
#        return allwords_dict
#    
#    
#    def generate_freq(words):
#        words_bi_gram = []
#        n = len(words)
#        for i in range(n-1):
#            words_bi_gram.append(" ".join([words[i],words[i+1]]))
#        word_freq = collections.Counter(words_bi_gram)
#        return word_freq
    
    
    #wordsfreuency=generate_wc_data(text50)
    FinalDf=pd.DataFrame()
    FinalDf = pd.DataFrame(np.array(text50))
    FinalDf=FinalDf.rename(index=str, columns={0: "Keyword"})
    #print(wordsfreuency)
    #FinalDf = pd.DataFrame.from_dict(wordsfreuency, orient='index').reset_index()
    print(FinalDf)
    #pathword=pathword[6:]
    FinalDf.to_csv(r"C:\Users\NDH00360\Desktop\Normalization\USPatentsCorpus\Compitetor\{}".format(pathword)+".csv")


