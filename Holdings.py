#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import numpy as np


# In[63]:


data = pd.read_csv('holdings.csv')


# In[66]:


invested_amount_total = round(sum(data['Qty.'] * data['Avg. cost']),3)


# In[68]:


pct_list = []
interim = data['Qty.'] * data['Avg. cost']
for i in interim:
    pct_list.append(round(((i / invested_amount_total) * 100),3))
data['Invested Amount Percentage'] = pct_list


# In[70]:


data.to_csv('holdings.csv')

