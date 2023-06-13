#!/usr/bin/env python
# coding: utf-8

# In[1]:



from sqlalchemy import create_engine

import pymysql

import pandas as pd


# In[2]:


a = "mysql+pymysql://root:NewPassword@localhost:3306"


# In[ ]:


sqlEngine       = create_engine(a, pool_recycle=3600)


# In[3]:


dbConnection    = sqlEngine.connect()


# In[ ]:


frame           = pd.read_sql("select * from besant.emp", dbConnection)


# In[ ]:


frame


# In[ ]:


frame['name'] = frame['name'].replace(["kishore"],"demo")


# In[ ]:


frame


# In[ ]:


frame.to_sql(con=dbConnection, schema = "besant" , name='emp', if_exists='replace', index=False)


# In[4]:


frame.to_sql(con=dbConnection, schema = "besant" , name='emp', if_exists='append', index=False)


# In[ ]:




