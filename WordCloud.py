# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:37:46 2019

@author: NDH00360
"""
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt



dfcloud = pd.read_csv(r"C:\Users\NDH00360\Desktop\comfortScorePerCategory.csv", index_col=0)

dfcloud=result.loc[result['assignee_name'].isin(["Toyota Motor Engineering & Manufacturing North America, Inc.","TOYOTA JIDOSHA KABUSHIKI KAISHA"])]
polaritygroup = dfcloud.groupby("Polarity")
polaritygroup.describe().head()

textcloud = dfcloud.Text[1]
#wordcloud = WordCloud().generate(textcloud)
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(textcloud)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

listcloud=[]

dfcloud1=dfcloud.groupby(['keyword','Polarity']).Text.apply(list).reset_index()
postivecloud=dfcloud1['Text'][1]
postivecloud=''.join(postivecloud)
negativecloud=dfcloud1['Text'][0]
negativecloud=''.join(negativecloud)

def Cloud(CarName,Polarity,textcloud):
    print(CarName,Polarity)
    stopwords = set(STOPWORDS)
    stopwords.update(["video","nice","car","one" ,"now", "looks", "great", "poor","Cars","review"])

    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(textcloud)


    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
#    return 0

for i in range(0,len(dfcloud1)):
    reviewremark=dfcloud1['Text'][i]
    reviewname=dfcloud1['keyword'][i]
    reviewPolarity=dfcloud1['Polarity'][i]
    reviewremark=''.join(reviewremark)    
    Cloud(reviewname,reviewPolarity,reviewremark)    


import matplotlib    
matplotlib.use('SVG') #set the backend to SVG
wordcloud.to_file("MyImage.svg")


plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off")
fig = plt.gcf() #get current figure
fig.set_size_inches(10,10)  

plt.savefig(r'C:\Users\NDH00360\Desktop\MyImage')

    


for words in wordcloud:
    print (words)