#!/usr/bin/env python
# coding: utf-8

# In[1]:


#indexing  postion
0   1  2  3  4  5
P   Y  T  H  O  N
-6 -5 -4 -3 -2 -1 


# In[3]:


#index position
a="Sachin Tendulkar";
print(a[5]);


# In[5]:


#characters between the index
print(a[3:10]);


# In[7]:


#index postion in reverse order
print(a[-1]);


# In[11]:


#index all the characters  
print(a[:])
print(a[::])


# In[13]:


#index with start: end:intervals postions
print(a[::3])


# In[27]:


#reversing the string
# by only changing the interval from reverse we can reverse the entire string
print(a[::-1]);
print(a[::-3]);


# In[29]:


#index postion of the variable in the array
print(a.index("S"));


# In[31]:


#a postion after interval 
print(a.index("a",3))


# In[33]:


#a position between start aand end value
print(a.index("a",0,3));


# In[35]:


#finding the postion from reverse of the string
print(a.rindex('a'));


# In[37]:


# find the postion of the element 
print(a.find("a"));


# In[39]:


#reverse finding the position of the element
print(a.rfind("a"));


# In[41]:


#index postion of the element not in the string
print(a.index("z"))


# In[43]:


#finding the postion of the element not in the string returns -1
print(a.find("z"));


# In[45]:


#
print(a.find("z"))


# In[47]:


#reverse index of the element not in the string
print(a.rindex("z"))


# In[48]:


#find the element not in the string returns -1
print(a.rfind("z"))


# In[50]:


#count the times of element repeated in the string
print(a.count("a"))


# In[52]:


# spliting the mentioned element from the string
print(a.split("a"))


# In[56]:


#replacing the element mentioned
print(a.replace("a","$"))


# In[59]:


#splitting the element in the mentioned time
print(a.split("a",1))


# In[61]:


#replacing the element in the mentioned time
print(a.replace("a","$",1))


# In[63]:


a="Welcome to the Class"
#capitalize as a tile
print(a.title())
#capitializing only the first element
print(a.capitalize())


# In[72]:


a=123
#type of the data type
print(type(a))
#verfying the data type
print(isinstance(a,int))


# In[75]:


a="123"
#data type
print(type(a))
#checking the data type
print(isinstance(a,int))
#checking is digit or not
print(a.isdigit())


# In[85]:


#converting the data type (tyepcasting)
print(int(a))
a=123
#converting the floating value
print(float(a))
#converting into octal decimal
print(oct(a))
#converting into the hexadecimal 
print(hex(a))


# In[ ]:




