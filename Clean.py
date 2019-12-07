# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:15:07 2019

@author: DELL
"""

import numpy as np
import pandas as pd
dataset=pd.read_csv('new.csv',delimiter='\t', quoting=3,encoding='latin-1')
#print(dataset)
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,1000):
 
    sim=re.sub('[^a-zA-Z]',' ',dataset['blog_context'][i])
    sim=sim.lower()
    sim=sim.split()
    ps=PorterStemmer()
    sim=[ps.stem(word) for word in sim if not word in  set(stopwords.words('english'))]
    sim= ' '. join(sim)
    corpus.append(sim)


