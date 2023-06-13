#!/usr/bin/env python
# coding: utf-8

# In[8]:



a= {"name" : "dinesh", "age" : 12, "loc" : "chennai"}

print(type(a))


# In[10]:


print(isinstance(a,list))
print(min(a))
print(max(a))
print(sorted(a))


# In[13]:


#value prints the values as list
print(a.values())


# In[12]:


#items prints both the keys and values
print(a.items())


# In[15]:


#keys prints the keys as the list
print(a.keys())


# In[17]:


#obtaining the values by using the key
print(a['name'])
print(a.get('name'))


# In[19]:


#for keys that  are not present
print(a['demo'])


# In[21]:


print(a.get('demo'))


# In[23]:


#for printing the other values 
print(a.get('demo','dummy'))


# In[32]:


#for adding new value in dict
a['demo']='test'
print(a)


# In[33]:


#for a values in dict
del a["demo"]
print(a)


# In[40]:


a = {'name': 'dinesh', 'age': 12, 'loc': 'chennai', 'name': 'kumar'}
print(a)


# In[39]:


a["name"]="kiran"
print(a)


# In[41]:


##operators


# In[43]:


#arithmetic
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b) #floor divison gives the qiotient of the function
print(a%b)#Modulo operator gives the remainder


# In[45]:


#ASSIGN OPERATOR 
a=5
b=3
print(a==b)
print(a!=b)
print(a<b)
print(a<=b)
print(a>=b)
print(a>b)
#


# In[47]:


#logical operator
print(True and True)
print(False and True)
print(True or False)
print(True or True)

