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
import asyncio

from tkinter import *





#from nltk.tokenize import word_tokenize


# In[2]:


pattern = r'[' + string.punctuation +']'


# In[3]:


#sentences = ("Trong khi đó, trong kỳ họp Quốc hội bất thường khai mạc ngày 4/1, Chính phủ có trình Quốc hội dự thảo một luật sửa 8 luật (trong đó có Luật Đầu tư), nhưng lại không có nội dung về sửa đổi phân cấp, phân quyền chấp thuận chủ trương đầu tư xây dựng khu công nghiệp. 'Chúng tôi đề nghị Chính phủ bổ sung vấn đề này vào để sớm sửa quy định. Đi theo với sự phân cấp, phân quyền là tăng cường kiểm tra, giám sát, cá thể hóa trách nhiệm', ông Quảng đề xuất. Được mời phát biểu, Chủ tịch UBND TP.HCM Phan Văn Mãi cũng nhắc đến một luật sửa 8 luật đang được Chính phủ trình Quốc hội. Ông đề nghị sau khi Quốc hội thông qua thì Chính phủ sớm có hướng dẫn, phân cấp, phân quyền để luật đi vào cuộc sống. Những vấn đề cần phân cấp, phân quyền được Chủ tịch UBND TP.HCM đề xuất là phê chuẩn, điều chỉnh cục bộ quy hoạch, tách dự án giải phóng mặt bằng ra khỏi dự án thông thường... Lãnh đạo TP.HCM cũng đề nghị, kiến nghị sớm sửa đổi Luật Đất đai. Là tham luận cuối cùng trong buổi sáng, Bí thư Thành ủy Thái Nguyên Nguyễn Thanh Hải cũng đề nghị quan tâm phân cấp, phân quyền nhiều hơn cho địa phương. Bà Hải đặc biệt nhấn mạnh đến việc triển khai tách dự án giải phóng mặt bằng ra khỏi dự án thông thường, như vậy mới có thể tạo sự đột biến trong việc thu hút đầu tư.")


# In[4]:



def btn_clicked():
    scale_value = scale.get()
    entry1.delete('1.0', END)
    
    sentences = entry0.get("1.0", "end-1c")
    print(sentences)
    if sentences == '':
        print('empty')
        entry1.insert(END, "Empty..")
    else:
        OUTPUT = summarize(sentences, scale_value)
    
        entry1.delete('1.0', END)
        entry1.insert(END, OUTPUT)
    
    
    
    


# In[5]:


def summarize(sentences, scale_value):
    #Number of words in input text
    words_in = ViTokenizer.tokenize(sentences)
    words_in = re.sub(pattern, '', words_in)
    number_of_words_in = len(words_in.split())
    
    #split sentences - lowercase
    #sentences=sentences.lower().strip()
    sentences=sentences.strip()
    
    sentences = nltk.sent_tokenize(sentences)
    #print(sentences)
    number_of_sentences = len(sentences)
    
    
    import sklearn.model_selection
    from gensim.models import KeyedVectors 
    w2v = KeyedVectors.load_word2vec_format("Vectors-sg/vi-300-5-40000-5-fullsplit-sg-token.vec")
    
    vocab = w2v.vocab
    
    sentences_vec_array = []
    for sentence in sentences:
        sentence = re.sub(pattern, '', sentence)
        sentence = ViTokenizer.tokenize(sentence).strip()
        words = sentence.split()
        sentence_vec = np.zeros((300))
        for word in words:
            if word in vocab:
                sentence_vec+=w2v.wv[word]
        sentences_vec_array.append(sentence_vec)
        
    #cluster
    from sklearn.cluster import KMeans

    #n_clusters = 5
    n_clusters = round((number_of_sentences/5)*scale_value)
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(sentences_vec_array)
    
    #choose sentence for each cluster
    from sklearn.metrics import pairwise_distances_argmin_min

    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))

    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, sentences_vec_array)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = '\n'.join([sentences[closest[idx]] for idx in ordering])
    
    #Number of words in final text
    words_out = ViTokenizer.tokenize(summary)
    number_of_words_out = len(words_out.split())
    
    
    #print("tom tat: ")
    #print(words_out)
    print(summary)
    print("Number_of_sentences: " + str(number_of_sentences))
    print("number_of_words_in: " + str(number_of_words_in))
    print("number_of_words_out: " + str(number_of_words_out))
    print("div: " + str((number_of_words_out/number_of_words_in)*100))
    print("number_of_cluster: " + str(n_clusters))
    return summary
    
    
    


# In[6]:


if __name__ == "__main__":
    window = Tk()

    window.geometry("1005x571")
    window.configure(bg = "#ffffff")
    window.title("Auto Text Summarization")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 571,
        width = 1005,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"GUI/background.png")
    background = canvas.create_image(
        496.5, 291.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"GUI/img_textBox0.png")
    entry0_bg = canvas.create_image(
        253.5, 280.5,
        image = entry0_img)

    entry0 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry0.place(
        x = 35.0, y = 56,
        width = 437.0,
        height = 457)

    entry1_img = PhotoImage(file = f"GUI/img_textBox1.png")
    entry1_bg = canvas.create_image(
        754.5, 280.5,
        image = entry1_img)

    entry1 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry1.place(
        x = 536.0, y = 56,
        width = 437.0,
        height = 457)
    
    scale = Scale(
        window,
        from_=1,
        to=3,
        orient = 'horizontal',
        length = 150,)
    scale.place(x = 115, y = 5)
    
    label = Label(window, text = "Mức độ tóm tắt:")
    label.place(x = 25, y = 5)

    img0 = PhotoImage(file = f"GUI/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(),
        relief = "flat")

    b0.place(
        x = 200, y = 525,
        width = 108,
        height = 39)
    
    window.resizable(False, False)
    window.mainloop()


# In[6]:





# In[ ]:





# In[ ]:





# In[ ]:


def UI():

    window = Tk()

    window.geometry("1005x571")
    window.configure(bg = "#ffffff")
    window.title("Auto Text Summarization")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 571,
        width = 1005,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"GUI/background.png")
    background = canvas.create_image(
        496.5, 291.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"GUI/img_textBox0.png")
    entry0_bg = canvas.create_image(
        253.5, 280.5,
        image = entry0_img)

    entry0 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry0.place(
        x = 35.0, y = 56,
        width = 437.0,
        height = 457)

    entry1_img = PhotoImage(file = f"GUI/img_textBox1.png")
    entry1_bg = canvas.create_image(
        754.5, 280.5,
        image = entry1_img)

    entry1 = Text(
        bd = 0,
        bg = "#feffff",
        highlightthickness = 0)

    entry1.place(
        x = 536.0, y = 56,
        width = 437.0,
        height = 457)
    
    scale = Scale(
        window,
        from_=1,
        to=3,
        orient = 'horizontal',
        length = 150,)
    scale.place(x = 115, y = 5)
    
    label = Label(window, text = "Mức độ tóm tắt:")
    label.place(x = 25, y = 5)

    img0 = PhotoImage(file = f"GUI/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:btn_clicked(),
        relief = "flat")

    b0.place(
        x = 200, y = 525,
        width = 108,
        height = 39)
    
    window.resizable(False, False)
    window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




