#!/usr/bin/env python
# coding: utf-8

# In[1]:


#OOPS CONCEPT
##INHERITANCE


# In[2]:


#single
#parent and child only
class clac():
    def add(self,a,b):
        print(a+b)


# In[7]:


class clac1(clac):
    def sub(self,a,b):
        print(a-b)


# In[8]:


a =clac1()
a.add(5,4)
a.sub(9,8)


# In[10]:


#Multi Level Inheritance
#it includes parent child and grandchild
class clac():
    def add(self,a,b):
        print(a+b)
        
class clac1(clac):
    def sub(self,a,b):
        print(a-b)
        
class clac2(clac1):
    def mult(self,a,b):
        print(a*b)  
        
a= clac2()
a.add(8,3)
a.sub(9,4)
a.mult(4,5)


# In[25]:


#Multiple level Inhertiance
#it includes the parent child and grandchild
#the parent is again mention in the grandchild
class clac():
    def add(self,a,b):
        print(a+b)
        
class clac1(clac):
    def sub(self,a,b):
        print(a-b)
        
class clac2(clac1,clac):
    def mult(self,a,b):
        print(a*b)  
        
a= clac2()
a.add(8,3)
a.sub(9,4)
a.mult(4,5)


# In[26]:


#Hierrachial inheritance
#includes parent child and grand child
#parent is mentioned in both child and grand child
class clac():
    def add(self,a,b):
        print(a+b)
        
class clac1():
    def sub(self,a,b):
        print(a-b)
        
class clac2(clac):
    def mult(self,a,b):
        print(a*b)  
        
a= clac2()
a.add(8,3)
#the sub doesnt inherit because the grand child doesnt inherit the child
a.sub(9,4)
a.mult(4,5)


# In[15]:


#Inheritance with constructor
#single
class parent():
    def __init__(self):
        self.name="parent"
class child(parent):
    def __init__(self):
        self.child="child"
        super().__init__()
        
        def test(self):
            pass
a= child()
a.name


# In[19]:


#Multi level inheritnace using constructor
class parent():
    def __init__(self):
        self.name="parent"
class child(parent):
    def __init__(self):
        self.child="child"
        super().__init__()
class gchild(child):
    def __init__(self):
        self.gchild="gchild"
        super().__init__()
        
        
        def test(self):
            pass
a= gchild()
print(a.name)
print(a.child)


# In[24]:


#Multiple level inheritance with constructor
class parent():
    def __init__(self):
        self.name="parent"
class child():/
    def __init__(self):
        self.child="child"
        
class gchild(parent,child):
    def __init__(self):
        self.gchild="gchild"
        super().__init__()
        super(parent,self).__init__()
        
    def test(self):
            pass
a= gchild()
print(a.name)
print(a.child)


# In[27]:


#the abstract method is used to pass along the method to the whole inheritance 
   #it is used to recall the function in every class passsed to every class
   #the abstract method should be passed along in the every class in methods
   from abc import ABC , abstractmethod

class parent(ABC):
   
   @abstractmethod
   def add(self):
       pass
   @abstractmethod
   def sub(self):
       pass
   
   def div(self):
       pass
class calc(parent):
   
     
   def add(self,a,b):
       print(a+b)
    
   def sub(self,a,b):
       print(a-b)
   def mul(self,a,b):
       print(a*b)
a = calc() 


# In[ ]:


|

