#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BREAK
for i in range(5):
    
    if i == 3:
        break
    print(i)


# In[2]:


#CONTINUE
for i in range(5):
    
    if i == 3:
        continue
    print(i)


# In[3]:


#PASS
for i in range(5):
    
    if i == 3:
        pass
    print(i)


# In[4]:


class test():
    "this is used for"
    
    def test(self):
        pass


# In[5]:


a = test()
a.__doc__


# In[6]:


x = 5

#if condition returns False, AssertionError is raised:
assert x < 4, "x should be 'less than 4"


# In[10]:




a = open("welcome.txt" , "r")
for i in a:
    print(i)


# In[11]:


a = open("welcome.txt" , "r")
a = a.readlines()
print(a)


# In[12]:


a = open("welcome.txt" , "r")
a = a.read()
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


import pandas as pd

data = pd.read_csv("dinesh.csv")


# In[ ]:


data.to_csv("ajdhajsgd.csv")


# In[15]:


#EXPECTION HANDLING
a = 5
b = 0
print(a/b)


# In[17]:


a = 5
b = "test"
try:
    print(a/b)
except ZeroDivisionError:
    b = 1
    print(a/b)
# except TypeError:
#     a = 1
#     b = 1
#     print(a/b)
except Exception as e:
    raise(e)


# In[18]:


a = 5
b = "test"
if a == 5:
    raise("error")


# In[19]:


class dinesh(Exception):
    
    def __str__(self):
        return("dinesh error")


# In[20]:


if a== 5:
    raise dinesh


# In[21]:


for i in range(5):
    
    print(i)


# In[22]:


#ITERATOR
a = iter(range(5))
print(next(a))


# In[23]:


print(next(a))


# In[24]:


print(next(a))


# In[25]:


print(next(a))


# In[26]:


print(next(a))


# In[27]:


print(next(a))


# In[28]:


#ITERATOR


# In[32]:


def test():
    l = []
    for i in range(5):
        l.append(i)
    return l


# In[ ]:


#GENERATOR
def test():
    
    for i in range(5):
        yield i


# In[35]:


a = test()


# In[36]:


print(next(a))


# In[37]:


#DECORATOR
def test(a,b):
    if a<b:
        a,b = b,a
    print(a/b)
test(2,4)


# In[38]:


##decorator
def dmasgjhgs(dddd):
    print("inside dec",dddd)
    def inner(a,b):
        print("inside dec func")
        if a <b:
            a,b = b,a
        return dddd(a,b)
    return inner


# In[39]:


@dmasgjhgs
def test(a,b):
    print("inside real fncts")
    print(a/b)


# In[40]:


test(4,2)


# In[ ]:




