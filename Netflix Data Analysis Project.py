#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


n = pd.read_csv("D:\\Python\\Data Science\\netflix_titles.csv")


# In[7]:


n


# In[9]:


n.head()


# In[10]:


n.shape


# In[11]:


n.tail()


# In[12]:


n.size # shows number of elements in this data set


# In[13]:


n.columns


# In[14]:


n.dtypes


# In[15]:


n.info()


# In[16]:


## Finding if there is any duplicate record present or not

## If yes remove it


n.head()


# In[17]:


n.shape


# In[18]:


n.duplicated() # Checking duplicate enteries


# In[19]:


n[n.duplicated()]


# In[20]:


# Checking the null values 

n.isnull()


# In[21]:


n.isnull().sum()  # Column wise null values


# In[22]:


# Heat Map of null values

import seaborn as sns


# In[23]:


sns.heatmap(n.isnull())


# In[24]:


n.head()


# In[26]:


n['title']


# In[27]:


# Checking whether the House of Cards show is present in the dataframe or not
n['title'].isin(['House of cards'])


# In[28]:


n[n['title'].isin(['House of cards'])]


# In[29]:


# Checking whether the Kota Factory show is present in the dataframe or not

n[n['title'].isin(['Kota Factory'])]


# In[30]:


n['title'].str.contains('Kota Factory')


# In[31]:


n[n['title'].str.contains('Kota Factory')]


# In[33]:


n.dtypes


# In[34]:


# Copied date added column to Date N column with data-time format

n['Data_N'] = pd.to_datetime(n['date_added'])


# In[35]:


n.head()


# In[36]:


n.dtypes


# In[40]:


# Counts all the occurrence of all individual years in date column

n['Data_N'].dt.year.value_counts()


# In[41]:


n['Data_N'].dt.year.value_counts().plot(kind='bar')


# In[42]:


# Showing how many movies and tv shows are there in the dataset.

n.head(3)


# In[43]:


# Grouping all the unique items of a column and show their count

n.groupby('type')


# In[44]:


n.groupby('type').type.count()


# In[45]:


sns.countplot(n['type'])


# In[46]:


# Showing all the movies released in the year 2019

n.head()


# In[47]:


n['Year'] = n['Data_N'].dt.year


# In[48]:


n


# In[50]:


n[(n['type'] == 'Movie') & (n['Year'] ==  2019)]


# In[51]:


n[(n['type'] == 'Movie') & (n['Year'] ==  2019)].head()


# In[52]:


# Showing all the titles of all the tv shows that were released in India Only
# and Movies in USA
n.head(4)


# In[59]:


(n['type'] == 'Movie') & (n['country'] == 'United States')


# In[60]:


n[(n['type'] == 'TV Show') & (n['country'] ==  'India')]


# In[61]:


n[(n['type'] == 'Movie') & (n['country'] == 'United States')]


# In[62]:


n[(n['type'] == 'Movie') & (n['country'] == 'United States')]['title']


# In[64]:


n[(n['type'] == 'TV Show') & (n['country'] == 'India')]['title']


# In[65]:


n.head(4)


# In[67]:


# Showing the results of top 10 Directors who gave the highest number of TV Shows & Movies to Netflix

n['director'].value_counts()


# In[68]:


n['director'].value_counts().head(10)


# In[69]:


# Showing all the records where type is movies, listed_in as comedies or country is united kingdom

n.head()


# In[70]:


n[(n['type'] == 'Movie') & (n['listed_in'] == 'Comedies')]


# In[71]:


n[(n['type'] == 'Movie') & (n['listed_in'] == 'Comedies') | (n['country'] == 'United Kingdom')]


# In[76]:


# Movies  or shows in which Tom Cruise was casted in

n['cast'].str.contains('Tom Cruise')


# In[77]:


m = n.dropna()
m


# In[78]:


m.head()


# In[79]:


m[m['cast'].str.contains('Tom Cruise')]


# In[80]:


# Different ratings defined by netflix

n['rating'].nunique()


# In[81]:


n['rating'].unique()


# In[82]:


# How many Movies got the TV-MA rating in Canada

n.head()


# In[83]:


(n['type'] == 'Movie') & (n['rating'] == 'TV-MA')


# In[84]:


n[(n['type'] == 'Movie') & (n['rating'] == 'TV-MA')]


# In[85]:


n[(n['type'] == 'Movie') & (n['rating'] == 'TV-MA')].shape


# In[86]:


n[(n['type'] == 'Movie') & (n['rating'] == 'TV-MA') & (n['country'] == 'Canada')]


# In[87]:


n[(n['type'] == 'Movie') & (n['rating'] == 'TV-MA') & (n['country'] == 'Canada')].shape


# In[88]:


# TV Shows that got the R rating after 2019

(n['type'] == 'TV Show') & (n['rating'] == 'R')


# In[89]:


n[(n['type'] == 'TV Show') & (n['rating'] == 'R')]


# In[96]:


n[(n['type'] == 'TV Show') & (n['rating'] == 'R') & (n['Year'] > 2018)]


# In[97]:


# Maximum duration of a movie / Show on Netflix

n.duration.unique()


# In[98]:


n.duration.nunique()


# In[99]:


# Considering only the duration in mins

n.duration.dtypes


# In[102]:


n[['Minutes', 'Unit']] = n['duration'].str.split(' ', expand = True)


# In[103]:


n[['Minutes', 'Unit']]


# In[110]:


n['Minutes'].max


# In[108]:


n[['Minutes', 'Unit']].max()


# In[111]:


# Individual Country with the highest number of TV Shows

n.head(2)


# In[112]:


tv = n[n['type'] == 'TV Show']
tv


# In[113]:


tv['country'].value_counts()


# In[114]:


# Sorting the dataset by year

n.sort_values(by='Year')


# In[115]:


n.sort_values(by='Year').head(5)


# In[117]:


n.sort_values(by='Year', ascending = False)


# In[118]:


n.sort_values(by='Year', ascending = False).head()


# In[120]:


# Instances where type is Movie and listed_in as dramas

n[((n['type'] == 'Movie') & (n['listed_in'] == 'Dramas') | (n['type'] == 'Movie') & (n['listed_in'] == 'Dramas'))]


# In[121]:


n[((n['type'] == 'Movie') & (n['listed_in'] == 'Dramas') | (n['type'] == 'Movie') & (n['listed_in'] == 'Dramas'))].head()


# In[129]:


(n['type'] == 'TV Show') & (n['listed_in'] == "Kids' TV")


# In[130]:


n[ (n['type'] == 'TV Show') & (n['listed_in'] == "Kids' TV")]


# In[ ]:





# In[ ]:




