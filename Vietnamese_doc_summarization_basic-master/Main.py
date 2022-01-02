#!/usr/bin/env python
# coding: utf-8

# # Import library

# In[1]:


import pickle
import numpy as np
from pyvi import ViTokenizer


# # Loading data

# In[2]:


#Load
with open ('neg.pkl', 'rb') as fp:
    contents = pickle.load(fp)


# In[3]:


#Pre-processing
contents_parsed = []
for content in contents[0:10]:
    contents_parsed.append(content.lower().strip())


# In[4]:


textindex=9


# In[ ]:





# In[5]:


print(contents[textindex])


# In[6]:


#print(contents_parsed[textindex])


# # Sentences Tokenizer

# In[7]:


import nltk
nltk.download('punkt')


# In[8]:


sentences = nltk.sent_tokenize(contents_parsed[textindex])


# In[9]:


#sentences = nltk.sent_tokenize('Abraham mở tỷ số ngay phút đầu tiên với pha dứt điểm trong tư thế đang ngã lộn cổ xuống đất. Cũng với pha phản công nhanh, Nicolo Zaniolo nâng tỷ số lên 2-0 ở phút 27 với cú đá về góc hẹp trong thế đối mặt. Đây là bàn đầu của Zaniolo ở Serie A mùa này, và anh cũng đề cao Mourinho khi nói: "Chúng tôi đã làm đúng như Mourinho yêu cầu, đó là thủ chặt và phản công nhanh. Đây mới là sức mạnh thật sự của Roma, chứ không phải như ở trận thua Inter".')


# In[10]:


print(sentences)


# # Sentences to vector

# In[11]:


import sklearn.model_selection
from gensim.models import KeyedVectors 


w2v = KeyedVectors.load_word2vec_format("vi1.vec")


# In[12]:


vocab = w2v.vocab


# In[13]:


X = []
for sentence in sentences:
    sentence = ViTokenizer.tokenize(sentence)
    words = sentence.split(" ")
    sentence_vec = np.zeros((300))
    for word in words:
        if word in vocab:
            sentence_vec+=w2v.wv[word]
    X.append(sentence_vec)


# In[14]:


###

from sklearn.cluster import KMeans

n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters)
kmeans = kmeans.fit(X)


# In[15]:


from sklearn.metrics import pairwise_distances_argmin_min

avg = []
for j in range(n_clusters):
    idx = np.where(kmeans.labels_ == j)[0]
    avg.append(np.mean(idx))
closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
ordering = sorted(range(n_clusters), key=lambda k: avg[k])
summary = ' '.join([sentences[closest[idx]] for idx in ordering])


# In[16]:


summary


# In[ ]:




