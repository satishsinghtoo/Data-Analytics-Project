#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install kaggle')


# In[3]:


import kaggle
get_ipython().system('Kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[4]:


import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() 
zip_ref.close() 


# In[9]:


import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[10]:


df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[11]:


df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price'] = df['list_price']-df['discount']
df['profit'] = df['sale_price']-df['cost_price']
df


# In[12]:


df.dtypes


# In[13]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[15]:


df.dtypes


# In[16]:


df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[17]:


df


# In[18]:


import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-LM1UUOP\SQLEXPRESS/master?driver=ODBC+Driver+17+for+SQl+Server')
conn=engine.connect()


# In[24]:


df.to_sql('df_orders', con=conn, index=False, if_exists= 'append')

