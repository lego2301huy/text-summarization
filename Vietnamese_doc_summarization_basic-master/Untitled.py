#!/usr/bin/env python
# coding: utf-8

# # Import lib

# In[1]:


import pickle
import numpy as np
import string
import re
from pyvi import ViTokenizer
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize


# In[2]:


pattern = r'[' + string.punctuation +']'


# In[3]:


sentences = ("Trong khi đó, trong kỳ họp Quốc hội bất thường khai mạc ngày 4/1, Chính phủ có trình Quốc hội dự thảo một luật sửa 8 luật (trong đó có Luật Đầu tư), nhưng lại không có nội dung về sửa đổi phân cấp, phân quyền chấp thuận chủ trương đầu tư xây dựng khu công nghiệp. 'Chúng tôi đề nghị Chính phủ bổ sung vấn đề này vào để sớm sửa quy định. Đi theo với sự phân cấp, phân quyền là tăng cường kiểm tra, giám sát, cá thể hóa trách nhiệm', ông Quảng đề xuất. Được mời phát biểu, Chủ tịch UBND TP.HCM Phan Văn Mãi cũng nhắc đến một luật sửa 8 luật đang được Chính phủ trình Quốc hội. Ông đề nghị sau khi Quốc hội thông qua thì Chính phủ sớm có hướng dẫn, phân cấp, phân quyền để luật đi vào cuộc sống. Những vấn đề cần phân cấp, phân quyền được Chủ tịch UBND TP.HCM đề xuất là phê chuẩn, điều chỉnh cục bộ quy hoạch, tách dự án giải phóng mặt bằng ra khỏi dự án thông thường... Lãnh đạo TP.HCM cũng đề nghị, kiến nghị sớm sửa đổi Luật Đất đai. Là tham luận cuối cùng trong buổi sáng, Bí thư Thành ủy Thái Nguyên Nguyễn Thanh Hải cũng đề nghị quan tâm phân cấp, phân quyền nhiều hơn cho địa phương. Bà Hải đặc biệt nhấn mạnh đến việc triển khai tách dự án giải phóng mặt bằng ra khỏi dự án thông thường, như vậy mới có thể tạo sự đột biến trong việc thu hút đầu tư.")


# In[4]:


print(sentences)


# In[5]:


#Number of words in input text
words_in = ViTokenizer.tokenize(sentences)
words_in = re.sub(pattern, '', words_in)
number_of_words_in = len(words_in.split())


# In[6]:


sentences=sentences.lower().strip()


# # Sentences Tokenizer

# In[7]:


sentences = nltk.sent_tokenize(sentences)
#print(sentences)
number_of_sentences = len(sentences)
#print(number_of_sentences)


# # # Sentences to vector

# In[8]:


import sklearn.model_selection
from gensim.models import KeyedVectors 


w2v = KeyedVectors.load_word2vec_format("Vectors/vi-300-5-20000-5-fullsplit.vec")


# In[9]:


vocab = w2v.vocab


# In[10]:


X = []
for sentence in sentences:
    sentence = ViTokenizer.tokenize(sentence)
    words = sentence.split(" ")
    sentence_vec = np.zeros((300))
    for word in words:
        if word in vocab:
            sentence_vec+=w2v.wv[word]
    X.append(sentence_vec)


# In[ ]:





# In[11]:


from sklearn.cluster import KMeans

n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters)
kmeans = kmeans.fit(X)


# In[12]:


from sklearn.metrics import pairwise_distances_argmin_min

avg = []
for j in range(n_clusters):
    idx = np.where(kmeans.labels_ == j)[0]
    avg.append(np.mean(idx))
closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
ordering = sorted(range(n_clusters), key=lambda k: avg[k])
summary = ' '.join([sentences[closest[idx]] for idx in ordering])


# In[13]:


summary


# In[14]:


print("tom tat: ")
print(summary)


# In[15]:


#Number of words in final text
words_out = ViTokenizer.tokenize(summary)
words_out = re.sub(pattern, '', words_out)
number_of_words_out = len(words_out.split())


# In[16]:


print("number_of_words_in: ")
print(number_of_words_in)


# In[17]:


print("number_of_words_out: ")
print(number_of_words_out)


# In[18]:


print("div: ")
print(round((number_of_words_out/number_of_words_in)*100))


# In[ ]:




