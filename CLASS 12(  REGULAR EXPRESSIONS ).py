#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


pattern = "^a...s$"


# In[3]:


if re.match(pattern , "addds"):
    print("yes")
else:
    print("no")


# In[4]:


pattern = "[abc]"

if re.match(pattern , "dinaesh"):
    print("yes")
else:
    print("no")


# In[5]:


pattern = "[a-zA-Z0-9]"

if re.match(pattern , "dinaesh"):
    print("yes")
else:
    print("no")


# In[6]:


pattern = "..."

if re.match(pattern , "DD"):
    print("yes")
else:
    print("no")


# In[7]:


pattern = "a*n"# zer0 or more occ of a .

if re.match(pattern , "ad"):
    print("yes")
else:
    print("no")


# In[8]:


pattern = "a?n"# zer or more occ
if re.match(pattern , "and"):
    print("yes")
else:
    print("no")


# In[9]:


pattern = "a{10,12}"

if re.match(pattern , "aaaaaaaaaaaaand"):
    print("yes")
else:
    print("no")


# In[10]:


pattern = "a|b"

if re.match(pattern , "nd"):
    print("yes")
else:
    print("no")


# In[11]:


pattern = "\w"

if re.match(pattern , "nAKJSDd11"):
    print("yes")
else:
    print("no")


# In[12]:


pattern = "\W"

if re.match(pattern , " nd"):
    print("yes")
else:
    print("no")


# In[13]:


pattern = "\d"

if re.match(pattern , "1234"):
    print("yes")
else:
    print("no")


# In[14]:


pattern = "\D"

if re.match(pattern , "1234"):
    print("yes")
else:
    print("no")


# In[15]:


pattern = "\s"

if re.match(pattern , " 1234"):
    print("yes")
else:
    print("no")


# In[16]:


pattern = "\S"

if re.match(pattern , "1234"):
    print("yes")
else:
    print("no")


# In[17]:


import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)


# In[18]:


import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)


# In[19]:


# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = '$$$$$$'

new_string = re.sub(pattern, replace, string) 
print(new_string)


# In[20]:


###
from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)


# In[21]:


import collections
# Create a deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)


# In[22]:


from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)


# In[23]:


from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)


# In[24]:


from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)


# In[25]:


from collections import Counter
 
# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("geeksforgeeks")
print(x)


# In[26]:


# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
	print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
	print(key, value)


# In[27]:


# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict

print("Before:\n")
od = {}
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
	print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
	print(key, value)


# In[ ]:




