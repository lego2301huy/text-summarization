# coding: utf-8
#!/usr/bin/python2
import nltk
import os
import codecs
import argparse
import numpy as np
import gensim # In case you have difficulties installing gensim, you need to consider installing conda.
from gensim.models.callbacks import CallbackAny2Vec
import pickle as pickle

# arguments setting 
parser = argparse.ArgumentParser()
parser.add_argument('--lcode', help='ISO 639-1 code of target language. See `lcodes.txt`.')
parser.add_argument('--vector_size', type=int, default=100, help='the size of a word vector')
parser.add_argument('--window_size', type=int, default=5, help='the maximum distance between the current and predicted word within a sentence.')
parser.add_argument('--vocab_size', type=int, default=10000, help='the maximum vocabulary size')
parser.add_argument('--num_negative', type=int, default=5, help='the int for negative specifies how many “noise words” should be drawn')
args = parser.parse_args()

lcode = args.lcode
vector_size = args.vector_size
window_size = args.window_size
vocab_size = args.vocab_size
num_negative = args.num_negative
epochs = 5

class callback(CallbackAny2Vec):
    '''Callback to print loss after each epoch.'''

    def __init__(self):
        self.epoch = 0
        self.loss_to_be_subed = 0
        self.losses = []

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        loss_now = loss - self.loss_to_be_subed
        self.loss_to_be_subed = loss
        print('Loss after epoch {}: {}'.format(self.epoch, loss_now))
        self.epoch += 1
        self.losses.append(loss_now)

def get_min_count(sents):
    '''
    Args:
      sents: A list of lists. E.g., [["I", "am", "a", "boy", "."], ["You", "are", "a", "girl", "."]]
     
    Returns:
      min_count: A uint. Should be set as the parameter value of word2vec `min_count`.   
    '''
    global vocab_size
    from itertools import chain
     
    fdist = nltk.FreqDist(chain.from_iterable(sents))
    min_count = fdist.most_common(vocab_size)[-1][1] # the count of the the top-kth word
    
    return min_count

def make_wordvectors():
    global lcode
    
     
    print ("Making sentences as list...")
    sents = []
    with codecs.open('data/corpus/vi-wiki.txt', 'r', 'utf-8') as fin:
    #with codecs.open('data/{}.txt'.format(lcode), 'r', 'utf-8') as fin:
        while 1:
            line = fin.readline()
            if not line: break
             
            words = line.split()
            sents.append(words)

    print ("Making word vectors...")   
    min_count = get_min_count(sents)

    call_back = callback()
    model = gensim.models.Word2Vec(sents, size=vector_size, min_count=min_count,
                                   negative=num_negative, 
                                   window=window_size,
                                   callbacks=[call_back],
                                   compute_loss=True,
                                   iter=epochs)
    
    # model.save('data/{}.bin'.format(lcode))
    model.wv.save_word2vec_format('data/vectors/{}-{}-{}-{}-{}-wiki.vec'.format(lcode, vector_size, window_size, vocab_size, num_negative), binary=False)
    
    # Save to file
    # with codecs.open('data/{}.vec'.format(lcode), 'w', 'utf-8') as fout:
    #     for i, word in enumerate(model.wv.index2word):
    #         fout.write(u"{}\t{}\t{}\n".format(str(i), word.encode('utf8').decode('utf8'),
    #                                           np.array_str(model[word])[1:-1]
    #                                           ))

    with codecs.open('data/vectors/{}-{}-{}-{}-{}-wiki.tsv'.format(lcode, vector_size, window_size, vocab_size, num_negative), 'w', 'utf-8') as fout:
        for i, word in enumerate(model.wv.index2word):
            fout.write(u"{}{}\n".format(word.encode('utf8').decode('utf8'),
                                              np.array_str(model[word])[1:-1]
                                              ))
if __name__ == "__main__":
    make_wordvectors()
    
    print ("Done")
