#!/usr/bin/env python
# coding: utf-8

# In[2]:


l=[]
a=["apple" ,"apple", "mango", "orange"]
for i in a:
    if i not in l:
        l.append(i)
for i in l:
    print(i)


# In[6]:


#import json
lis=[] #open list container 
#list of items
a=["apple" ,"apple", "mango", "orange"]
for i in a:
    if a.count(i) >0:
        #if i not in lis:
            lis.append(i)
            
(print("apple:",lis.count("apple")))
(print("mango:",lis.count("mango")))
(print("orange:",lis.count("orange")))

print(lis)


# In[1]:


lis=[]
a=["apple" ,"apple", "mango", "orange"]
for i in a:
     if a.count(i)==1:
        lis.append(i)
print(lis)
        #print(i)


# In[4]:


lis=[] #open list container 
#list of items
a=["apple" ,"apple", "mango", "orange"]
for i in a :
    if a.count(i) >1:
        #if i not in lis:
        print(i)
            


# In[5]:


a.count("apple")


# In[ ]:





# In[ ]:





# In[ ]:




