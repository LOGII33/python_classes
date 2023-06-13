#!/usr/bin/env python
# coding: utf-8

# In[1]:


#class and #object


# In[2]:


class truck():
    def engine(self):
        print("truck engine")
    def chasis(self):
        print("truck chasis")


# In[3]:


class car():
    def engine(self):
        print("car engine")
    def chasis(self):
        print("car chasis")
    


# In[4]:


#assigning a class to a variable,that variable is called %%object
a=truck()
print(a)


# In[5]:


a.engine()


# In[6]:


b=car()
print(b)


# In[7]:


b.chasis()


# In[8]:


a=car


# In[9]:


#dir gives directory of the inbuilt function in the class
dir(a)


# In[10]:


class hotel():
    def floor(self,a):
        if a==1:
            print("veg")
        elif a==2:
            print("non veg")
    def dish(self,a):
        if a==1:
            print("veg dish")
        elif a==2:
            print("non veg dish")
            
a=hotel()
a.floor(1)
a.dish(2)


# In[15]:


class hotel():
    #__init__ constructor variable used for initialization before the class
    def __init__(self,a):
        self.a=a
    def floor(self):
        if self.a==1:
            print("veg")
        elif self.a==2:
            print("non veg")
    def dish(self):
        if self.a==1:
            print("veg dish")
        elif self.a==2:
            print("non veg dish")
a=hotel(1)
a.floor()
a.dish()            


# In[20]:


#gold rate
class gold_rate():
    def __init__(self,price):
        self.price=price
    def total(self,gram):
        return self.price*gram
    
a=gold_rate(100)
a.total(5)
        
        


# In[ ]:


#fruit 
class fruit_classification():
    def __init__(s)

