#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[13]:


data.info()


# In[15]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[17]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[ ]:


data[

