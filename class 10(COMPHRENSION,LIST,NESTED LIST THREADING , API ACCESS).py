#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list comprehension
l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i)
print(l)


# In[2]:


a = [i for i in range(10) if i % 2 == 0]
print(a)


# In[3]:


a = [i for i in range(10) ]
print(a)


# In[4]:


#nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]
matrix


# In[5]:


matrix = []

for i in range(5):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)


# In[6]:


#dict comprehension
a = { i: i**2 for i in range(5)}
print(a)


# In[8]:


#THREADING
import time

t1 = time.time()

def test():
    for i in range(5):
        print(i)
        time.sleep(.5)
test()
test()
test()
test()

t2 = time.time()
print(t2 - t1)


# In[10]:


#MULTITHREADING
import threading

t1 = time.time()

def test():
    for i in range(5):
        print(i)
        time.sleep(.5)
th1 = threading.Thread(target = test)
th2 = threading.Thread(target = test)
th3 = threading.Thread(target = test)
th4 = threading.Thread(target = test)
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
t2 = time.time()
print(t2 - t1)


# In[11]:


#API ACCESS REQUEST
import requests
city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4c4784f2061bb212c329a6c7fbca4069&units=metric'.format(city)
res = requests.get(url)
data = res.json()
print(data)


# In[12]:


data.get('coord').get('lon')


# In[14]:


api_url = "https://jsonplaceholder.typicode.com/todos"


# In[13]:


todo = {"userId": 1, "title": "Drink whey", "completed": False}
response = requests.put(api_url, json=todo)
response.status_code


# In[ ]:




