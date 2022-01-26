import numpy as np
from gensim.test.utils import datapath
from gensim.models import KeyedVectors 
# Load a word2vec model stored in the C *text* format.
w2v = KeyedVectors.load_word2vec_format('vi-300-5-20000-5-fullsplit.vec', binary=False)
#w2v = KeyedVectors.load('vi-300-5-20000-5-fullsplit.vec',  mmap='r')
vector = w2v['và']

vocab = w2v.vocab
print(vocab)

