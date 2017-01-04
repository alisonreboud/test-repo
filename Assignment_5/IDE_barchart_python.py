
# coding: utf-8

# In[27]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sf_crime.csv", sep=",")

data2 = data[['Category','DayOfWeek']]


# In[18]:

type(data2)


# In[31]:

mon=len(data2.groupby('DayOfWeek')['Category'].sum()['Monday'])
tues=len(data2.groupby('DayOfWeek')['Category'].sum()['Tuesday'])
wed=len(data2.groupby('DayOfWeek')['Category'].sum()['Wednesday'])
thurs=len(data2.groupby('DayOfWeek')['Category'].sum()['Thursday'])
fri=len(data2.groupby('DayOfWeek')['Category'].sum()['Friday'])
sat=len(data2.groupby('DayOfWeek')['Category'].sum()['Saturday'])
sun=len(data2.groupby('DayOfWeek')['Category'].sum()['Sunday'])


# In[34]:

mon, tues, wed, thurs, fri, sat, sun


# In[ ]:




# In[ ]:



