#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Encapsulation
####Types
#public : can be accessed anywhere in the class (inside/outside)
#protected  : can be used by the parent ans inherited class(starts with _)
#private  : can be used accessed inside the class alone(starts with __) used in both variable and functions


# In[2]:


class test():
    name="logii"
a=test()
print(a.name)


# In[3]:


a.name="logesh"
print(a.name)


# In[4]:


#private
class test():
    __name="logii"
a=test()
print(a.__name)


# In[8]:


##private
class test():
    __name="dinesh"
    def display(self):
        print(self.__name)
        
    def change(self,a):
        self.__name=a
        
        
a = test()        


# In[9]:


a.display()


# In[10]:


a.change("kumar")
a.display()


# In[13]:


#POLYMORPHISM
#Method overloading
class parent:
    def name(self):
        print("parent")
class child(parent):
    def name(self):
        print("child")
a = test()


# In[14]:


a = child()
a.name()


# In[15]:


#method over writing
class test():
    def add(self,a,b,c=1):
        print(a+b+c)
a= test()
a.add(5,10)


# In[20]:


#STATIC METHOD
class static():
    def method(self):
        print("method")
    def demo(self):
        print("demo")
    @staticmethod
    def hello():
        print("hello")
        
a = static() 
a.hello()


# In[21]:


#FILTER
#map
#reduce
def test(a):
    if a % 2 == 0:
        return True
    else:
        return False


# In[22]:


#filter
inp = [1,2,3,4,5,6,7,8,9]
print(list(filter(test,inp)))


# In[23]:


#map
inp = [1,2,3,4,5,6,7,8,9]
print(list(map(test,inp)))


# In[24]:


#reduce
from functools import reduce

def test(m,n):
    return m+n
inp = [1,2,3,4,5,6,7,8,9]
print(reduce(test,inp))


# In[ ]:




