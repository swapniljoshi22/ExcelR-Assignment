#!/usr/bin/env python
# coding: utf-8

# # Assignment No 1

# # Question no 7

# In[19]:


import pandas as pd
import matplotlib as plt
df=pd.read_csv("Q7.csv")
df


# In[41]:


df.mean()


# In[3]:


df.var()


# In[4]:


df.median()


# In[5]:


df.std()


# In[6]:


print('Range of points',df.Points.max()-df.Points.min())


# In[7]:


print('Range of score',df.Score.max()-df.Score.min())


# In[8]:


print('Range of Weigh',df.Weigh.max()-df.Weigh.min())


# In[9]:


df.mode()


# In[91]:


df.describe()


# In[10]:


df.boxplot(figsize=('5','5'))


# In[16]:


df.plot()


# In[21]:


df["Points"].hist()


# In[22]:


df["Score"].hist()


# In[23]:


df["Weigh"].hist()


# In[24]:


df.plot.line(x='Points',y='Score')


# In[25]:


df.plot.line(x='Points',y='Weigh')


# In[26]:


df.plot.scatter(x='Points',y='Score')


# In[27]:


df.plot.scatter(x='Points',y='Weigh')


# In[28]:


df.plot.hexbin(x='Points',y='Score')


# In[30]:


df.plot.area(x='Points',y='Score')


# In[35]:


df.plot.pie(x='Points',y='Score')


# In[36]:


df.plot.kde(x='Points',y='Score')


# In[37]:


df.plot.kde(x='Points',y='Weigh')


# # Question no 9_a
# 

# In[151]:


df9=pd.read_csv("Q9_a.csv")
df9


# In[48]:


df9.kurtosis()


# In[49]:


df9.skew()


# In[92]:


df9.describe()


# In[56]:


df9.plot.box()


# In[59]:


df9.plot.density()


# In[62]:


df9.plot.hexbin(x='Index',y='speed')


# In[65]:


df9.plot.hist(x='Index',y='speed')


# In[69]:


df9.plot.hist(y='dist')


# In[73]:


df9.plot.kde(y='speed')


# In[74]:


df9.plot.kde(y='dist')


# In[80]:


df9.plot.line(y='speed')


# In[81]:


df9.plot.line(y='dist')


# In[85]:


df9.plot.scatter(x='dist',y='speed')


# In[90]:


df9.hist("dist")


# In[89]:


df9.hist("speed")


# In[86]:


df9.plot.scatter(x='Index',y='speed')


# # Question no 9_b

# In[94]:


df_9b=pd.read_csv("Q9_b.csv")
df_9b.head()


# In[95]:


df_9b.skew()


# In[96]:


df_9b.kurtosis()


# In[97]:


df_9b.describe()


# In[98]:


df_9b.hist('SP')


# In[99]:


df_9b.hist('WT')


# In[103]:


df_9b.plot.bar(y='WT')


# In[104]:


df_9b.plot.box(y='WT')


# In[105]:


df_9b.plot.box(y='SP')


# In[107]:


df_9b.plot.density(y='WT')


# In[109]:


df_9b.plot.density(y='SP')


# In[112]:


df_9b.plot.hexbin(x='SP',y='WT')


# In[114]:


df_9b.plot.line(y='SP')


# In[115]:


df_9b.plot.line(y='WT')


# In[117]:


df_9b.plot.scatter(x='SP',y='WT')


# # Question no 20

# In[123]:


df20=pd.read_csv('Cars.csv')
df20.head()


# In[157]:


mpg=(df20['MPG']>38).sum()
total=len(df20)
print("Probability of (MPG>38)= {}".format(mpg/total))


# In[156]:


mpg=(df20['MPG']<40).sum()
total=len(df20)
print("Probability of (MPG<40)= {}".format(mpg/total))


# In[161]:


mpg=(((df20['MPG'])>20) & ((df20['MPG'])<50)).sum()
total=len(df20)
print("Probability of (20<MPG>50)= {}".format(mpg/total))


# In[ ]:





# In[ ]:




