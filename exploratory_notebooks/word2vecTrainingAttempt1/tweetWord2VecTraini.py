import spacy
import gensim
import os
import numpy as np
import pandas as pd
import itertools
import json
import re
import pymoji
import importlib
from nltk.tokenize import TweetTokenizer
import string
import time

tokenizer = TweetTokenizer()
start_time = time.time()

def remove_retweets(tweets_objs_arr):
    return [x["text"] for x in tweets_objs_arr if x['retweet'] != 'Y']

def convert_emojis(tweets_arr):
    return [pymoji.replaceEmojiAlt(x, trailingSpaces=1) for x in tweets_arr]

def tokenize_tweets(tweets_arr):
    result = []
    for x in tweets_arr:
        try:
            tokenized = tokenizer.tokenize(x)
            result.append([x.lower() for x in tokenized if x not in string.punctuation])
        except:
            pass
#             print(x)
    return result

class Tweets(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for root, directories, filenames in os.walk(self.dirname):
            for filename in filenames:
                if(filename.endswith('json')):
                    print(time.time())
                    with open(os.path.join(root,filename), 'r') as f:
                        data = json.load(f)
                        data_parsed_step1 = remove_retweets(data)
                        data_parsed_step2 = convert_emojis(data_parsed_step1)
                        data_parsed_step3 = tokenize_tweets(data_parsed_step2)
                        for data in data_parsed_step3:
                            yield data


sentences = Tweets('/Volumes/SDExternal2/datasets/data4democracy/discursive/2017/1/') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences, workers=2, window=5, sg = 1, size = 100, max_vocab_size = 2 * 10000000)
model.save('tweets_word2vec_2017_1_size100_window5')
print('done')
print(time.time() - start_time)

#model files are also on s3 -- gensim may or maynot need the 2nd and the 3rd files...
# https://s3.amazonaws.com/d4d-twitter-word2vec-models/tweets_word2vec_2017_1_size100_window5
# https://s3.amazonaws.com/d4d-twitter-word2vec-models/tweets_word2vec_2017_1_size100_window5.syn0.npy
# https://s3.amazonaws.com/d4d-twitter-word2vec-models/tweets_word2vec_2017_1_size100_window5.syn1neg.npy
