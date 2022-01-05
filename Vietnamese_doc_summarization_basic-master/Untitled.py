#!/usr/bin/env python
# coding: utf-8

# # Import lib

# In[16]:


import pickle
import numpy as np
from pyvi import ViTokenizer
import matplotlib.pyplot as plt


# In[17]:


import nltk
nltk.download('punkt')


# In[18]:


sentences = ("Cấp chủ quyền, phép xây dựng: 'Kẽ hở' để hành dân  Mua bán hợp pháp không được cấp chủ quyền; nhà ở hợp pháp không được cấp phép xây dựng, nhưng lại được phép bán lại... Đó là thực trạng tại một số địa phương thuộc TP HCM.  Tháng 11/2002, bà Bùi Ngọc Thuận mua một lô đất 81 m2 ở khu phố 6, thị trấn An Lạc, huyện Bình Chánh cũ (TP HCM) của bà Nguyễn Thị Nụ. Bà Thuận làm đơn xin được cấp chủ quyền nhà nhưng không được UBND thị trấn xác nhận với lý do mà cán bộ địa chính nêu ra (bằng giấy viết tay): Đất xin sử dụng có một phần bị ảnh hưởng bởi quy hoạch giải tỏa khu dân cư quận 3.  Sau nửa năm khiếu nại, tháng 5/2003, UBND thị trấn An Lạc xin lỗi bà Thuận vì để bà phải đi lại nhiều lần và hứa sẽ kiểm điểm cán bộ địa chính có thái độ không khiêm tốn khi tiếp nhận hồ sơ. Đồng thời, chính quyền thị trấn đồng ý xác nhận và chuyển hồ sơ của bà Thuận lên huyện.  Tại huyện, sau 2 tháng chờ đợi, hồ sơ của bà Thuận lại bị trả về với lý do vị trí xin sử dụng đất có một phần nằm trên đường dự phóng. Có lẽ bà Thuận cũng đành chấp nhận nếu không phát hiện căn nhà liền kề với khu đất mà bà xin hợp thức hóa đã được cấp chủ quyền vào tháng 11/2003.  Tháng 2 vừa qua, bà Thuận lại tiếp tục nộp hồ sơ xin được cấp chủ quyền. Lúc này khu vực nhà bà đã thuộc quận Bình Tân (tách ra từ huyện Bình Chánh), Phòng Quản lý đô thị (QLĐT) quận Bình Tân lại xác nhận vị trí sử dụng đất có một phần nằm trong lộ giới đường vành đai trong theo quy hoạch khu dân cư phía nam đường Hùng Vương được phê duyệt từ tháng 9/1997.   Trong khi đó, nếu áp dụng theo các quy định về cấp chủ quyền nhà hiện hành, lô đất của bà Thuận vẫn được cấp chủ quyền vì chỉ bị ảnh hưởng bởi một phần chứ không nằm hoàn toàn trong khu quy hoạch.  Tháng 3/2001, ông Hà Văn Trung ở phường 12, quận Gò Vấp mua một miếng đất rộng 35 m2 trong khu dân cư, có nguồn gốc hợp lệ và được chính quyền phường, quận xác nhận.   Do bức bách về chỗ ở, ông Trung xây tạm một căn nhà tường gạch, mái tôn trên miếng đất đã mua. Mới đây, khi biết chủ trương của thành phố là cấp chủ quyền nhà đại trà (chỉ trừ trường hợp vi phạm quy hoạch), ông Trung nộp hồ sơ lên quận nhưng bị trả về với lý do: nhà chưa kê khai năm 1999 và diện tích quá nhỏ dưới 35 m2 nên không giải quyết. Tuy nhiên, thành phố không hề quy định những trường hợp trên không được cấp chủ quyền.   Do bị ảnh hưởng bởi dự án mở rộng vòng xoay Điện Biên Phủ, gia đình bà Phan Thị Thanh (gồm 11 người) được bố trí hai lô đất A17 và A25, cư xá Nguyên Hồng, phường 11, quận Bình Thạnh. Tháng 12/2003, bà Thanh phải bán bớt lô A25 để có tiền trả tiền xây nhà trên lô A17. Người mua đất là ông Bùi Hy Long.   Khi tiến hành làm hồ sơ xin chuyển quyền sử dụng đất để làm tiếp thủ tục xin phép xây dựng, ông Long bất ngờ khi nhận được văn bản của Phòng QLĐT quận Bình Thạnh ghi rõ: Hiện nay chủ đầu tư (Công ty Thanh niên xung phong - chủ đầu tư dự án cư xá Nguyên Hồng) chưa bàn giao cơ sở hạ tầng cho UBND quận Bình Thạnh. Do đó, phòng QLĐT chưa thể xem xét cấp phép xây dựng trong khu vực này. Ông Long chỉ có quyền sử dụng đất hoặc chuyển nhượng quyền sử dụng đất của mình cho người khác. Trường hợp ông Long không đồng ý chuyển nhượng quyền sử dụng đất thì liên hệ phòng QLĐT gặp bà Loan trong vòng hai ngày để phòng QLĐT ngưng giải quyết và trả hồ sơ theo quy định.  Gia đình anh Nguyễn Hạnh Vũ ở quận Bình Thạnh cũng không được cấp phép xây dựng dù cầm trong tay tờ giấy hồng (chủ quyền nhà) đã hơn một năm. Lý do: căn nhà anh mua nằm trong quy hoạch khu dân cư liên phường 1, 2, 3, 14 do Kiến trúc sư trưởng thành phố phê duyệt tháng 2/1999 và đang được UBND quận Bình Thạnh điều chỉnh.   Tháng 2/2004, nghe tin sẽ bãi bỏ quy hoạch bất khả thi, anh Vũ làm lại đơn xin phép xây nhà nhưng phòng QLĐT yêu cầu anh chỉ sửa chữa nhà theo hiện trạng chứ không được phép xây.")


# In[19]:


#print(sentences)


# In[20]:


sentences=sentences.lower().strip()


# In[21]:


#print(sentences)


# # Sentences Tokenizer

# In[22]:


sentences = nltk.sent_tokenize(sentences)
#print(sentences)


# # # Sentences to vector

# In[23]:


import sklearn.model_selection
from gensim.models import KeyedVectors 


w2v = KeyedVectors.load_word2vec_format("vi-300-5-40000-5-fullsplit.vec")


# In[24]:


vocab = w2v.vocab


# In[25]:


X = []
for sentence in sentences:
    sentence = ViTokenizer.tokenize(sentence)
    words = sentence.split(" ")
    sentence_vec = np.zeros((300))
    for word in words:
        if word in vocab:
            sentence_vec+=w2v.wv[word]
    X.append(sentence_vec)


# In[26]:


#print(X)


# In[27]:


from sklearn.cluster import KMeans

n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters)
kmeans = kmeans.fit(X)


# In[28]:


from sklearn.metrics import pairwise_distances_argmin_min

avg = []
for j in range(n_clusters):
    idx = np.where(kmeans.labels_ == j)[0]
    avg.append(np.mean(idx))
closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
ordering = sorted(range(n_clusters), key=lambda k: avg[k])
summary = ' '.join([sentences[closest[idx]] for idx in ordering])


# In[29]:


summary
print(summary)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




