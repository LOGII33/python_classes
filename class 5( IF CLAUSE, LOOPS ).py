#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = "sachin"


# In[1]:


# clause 
#if statement or conditional statement 


# In[ ]:





# In[3]:


if name == "sachin":
    print("yes")


# In[6]:


# if , else condition
if name == "kohli":
    print("yes")
else:
    print("no")


# In[7]:


#if and elif condtion
name ="sachin"
score ="100"
if name == "sachin" and score == "100":
    print("century")
elif  name== "sachin" and score>50:
    print("above 50")
else :
    print("less than 100")


# In[8]:


# nested if condition
if name == "sachin":
    if score =="100":
        print("its a century")
else:
    print("not an 100")


# In[9]:


#nested and elif
if name == "sachin":
    if score =="100":
        print("its a century")
elif  name== "sachin" and score>50:
    print("above 50")
else :
    print("less than 100")       


# In[10]:


#assignment 
#signal, police
# signal red ,police no --- goo
#signal red ,police yes -- stop
#signal yellow ,police yes -- slow down
#signal yellow , police no -- go
#signal green -- go


# In[13]:


#LOOPS


# In[12]:


#WHILE LOOP
a =1
while a<5:
    print(a)
    a= a+1


# In[15]:


#FOR LOOP
a=["dinesh", "mathesh","ashish"]
for i in a:
    print(i)


# In[16]:


list(range (5))


# In[20]:


for i in range(4):
    print(i)


# In[24]:


a = {"name" : "test", "age": 12}
 


# In[25]:


for k,v in a.items():
   print(k,v)


# In[ ]:


#a =[]

