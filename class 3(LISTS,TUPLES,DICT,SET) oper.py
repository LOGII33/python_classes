#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lists \ tuples\ sets \ dictionary operations


# In[2]:


x=["mani",12,"chennai"]
type(x)


# In[3]:


isinstance(x,str)


# In[4]:


x[::-1]


# In[13]:


a=[10,45,2,100,78]
print(min(a))
print(max(a))
print(sorted(a))


# In[16]:


xx = ['mani',12,'krish']
print(min(xx))#error is appering because of different data type


# In[29]:


#list
c=['chennai',24,'logi']
c.append('united kingdom')


# In[30]:


c


# In[31]:


c.insert(2,"chatgpt")
c


# In[34]:


c.remove("logi")
c


# In[35]:


del c[1]
print(c)


# In[37]:


c.pop(1)


# In[38]:


c


# In[42]:


#shallow copy and #deep copy memory
#shallow copy - same memory shared upon so it will be changed
d =[1,2,3,4]
f=d
d.append(5)
print(d)
print(f)


# In[41]:


#deep copy -Different memory is used up,so that it will not be changed
gg=[1,2,3,4,5]
hh = gg.copy()
gg.append(6)
print(gg)
print(hh)


# In[43]:


#note:
#so find (),rfind(),rindex(), Functions will not work in "LIST" data type
#only index() function works out in LIST
h1 = ['helo', 'belo', 'lello']
h1
h1.index("bello")
h1.rindex("bello")


# In[44]:


#tuple
z1 =("dinesh","krishna","mani")
type(z1)


# In[45]:


isinstance(z1,tuple)


# In[46]:


z1.append("lello")#cannot be mutated in tuple


# In[47]:


#set
zq ={1,1,1,1,2,2,2,2,}
print(zq)


# In[48]:


type(zq)


# In[49]:


isinstance(zq,set)


# In[50]:


zq={1.2,3,4,5,6,}
sq= {3,56,24,32,76}


# In[52]:


zq.union(sq)


# In[53]:


zq.intersection(sq)


# In[54]:


zq.difference(sq)


# In[55]:


sq.difference(zq)


# In[56]:


# while using "issupperset" and "issubset" functions we have make sure that we give some same elements in both


# In[57]:


print(zq.issuperset(sq))


# In[58]:


print(sq.issuperset(zq))


# In[59]:


print(zq.issubset(sq))


# In[60]:


print(sq.issubset(zq))


# In[61]:


#consider the below scenario,
#using "append"  function in 2 lists
x1= [1,2,3]
x2 =[4,5,6,]
x1.append(x2)
print(x1)


# In[64]:


#using "extend" in 2 lists
x1= [1,2,3,]
x2= [4,5,6]
x1.extend(x2)
print(x1)


# In[65]:


#using "+" function in 2 lists
x1= [1,2,3,]
x2= [4,5,6]
x3 = x1+x2
print(x3)


# In[66]:


#q1
#original list input
b11 =["kiran","kiran","kumar"]
print(b11)


# In[71]:


b11.remove("kiran")


# In[72]:


#q1 = another method using embedded|inner nest kind of "list(set())" functions
b11_alt =["kiran","kiran","kumar"]
print(b11_alt)
list(set(["kiran","kiran","kumar"]))


# In[73]:


#q3
aa=[1,2,3]
bb=[4,5,6]
cc=[7,8,9]
aa.extend(bb)
print(aa)


# In[74]:


aa.extend(cc)
print(aa)


# In[75]:


#q2
ss ="test@gmail.com"
print(ss)


# In[76]:


result = ss[0:4]
print("the taken out world is",result)


# In[77]:


#q2 -another method! - using "split " function
ss = "test@gmail.com"
print(ss)
output = ss.split("@")
output
output = output[0]
output


# In[80]:


wq = ["mani", "mahesh","dinesh","harish","jyoth"]
print(wq)


# In[81]:


wq.pop()


# In[82]:


print(wq)


# In[84]:


wq.pop(2)


# In[85]:


print(wq)


# In[88]:


lis1 = [1,2,3]
tupe1 =(4,5,6)
lis1.append(tupe1)


# In[89]:


print(lis1)


# In[90]:


lis1.extend(tupe1)
print(lis1)


# In[91]:


lis =[1,2,3]
tupe= (45,67,32)
tupe.append(lis)


# In[ ]:




