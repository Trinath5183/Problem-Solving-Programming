#!/usr/bin/env python
# coding: utf-8

# # Assignment:

# In[3]:


# 1) [1,4,5,6,9] - 14569
def convert(s):
    x=0
    for i in range(len(s)):
        x=x*10+s[i]
    return x
s=[1,4,5,6,9]
convert(s)


# In[6]:


# 2) [1,4,5,6,9]  - 46 (Consider only even numbers from list)
def even(s):
    x=0
    for i in range(len(s)):
        if s[i]%2==0:
            x=x*10+s[i]
    return x
s=[1,4,5,6,9]
even(s)


# In[7]:


# 3. [1,2,3,4,5] - [1,4,3,16,5] (Consider only even number and square of it)
def square(s):
    for i in range (len(s)):
        if s[i]%2==0:
            s[i]=s[i]**2
    return s
s=[1,2,3,4,5]
square(s)


# In[36]:


# 4. [15,19,12,16,4] - [15,34,31,28,4] (Need to add previous number to current number)
def add(s):
    k=[]
    for i in range (len(s)):  
        if i==0 or i==len(s)-1:
                k.append(s[i])
        else:
            k.append(s[i]+s[i-1])
    return k 
s=[15,19,12,16,4]
add(s)


# In[ ]:




