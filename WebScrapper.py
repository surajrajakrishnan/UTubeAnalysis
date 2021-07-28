# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:26:43 2019

@author: NDH00360
"""
from newspaper import Article


Articleurl = 'https://igniteoutsourcing.com/automotive/top-connected-car-startups/'


article = Article(Articleurl)
article.download()

article.html
article.parse()
Aurthor=article.authors
ArticleText=article.text

article.nlp()

article.keywords

article.summary