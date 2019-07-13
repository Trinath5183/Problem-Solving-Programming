#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1. Draw a circle, In that half circle has to have Green color 
# and another half required to fill with orange color using Turtle Package.
import turtle as y
a=y.Turtle()
a.color("green")
a.begin_fill()
a.circle(130,360)
a.end_fill()
a.hideturtle()
a.color("orange")
a.begin_fill()
a.circle(130,180)
a.end_fill()
a.hideturtle()


# In[ ]:


# 2. Draw a Spirling Square with Pen color as 'Red'.
import turtle as y
a=y.Turtle()
a.pencolor('black')
for i in range (100):
    a.forward(i)
    a.left(91)
y.done()


# In[ ]:


# 3. Write a python programming to print the large digit from given number
def Large(n):
    large = 0
    while n != 0:
        r = n % 10
        if large < r:
            large = r
        n = n // 10
    return large
n=int(input("enter a number"))
Large(n)


# In[ ]:


#4. Write a python programming to print the Palindrome count between two limits
#Example:-
#Test cases:- Input:- 1 10   Output:- 9
#Test cases:- Input:- 11 100 Output:- 9 
def palindrome(n):
    s=0
    k=n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        return True
    else:
        return False
def Cnt(m,n):
    c=0
    for i in range(m,n):
        if palindrome(i)==True:
            c=c+1
    return c
m=int(input("enter m"))
n=int(input("enter n"))
Cnt(m,n)


# In[4]:


#5. Write a python programming to create and find the word count from given input file
# If the file is contains same word then you need to print the output count

def createfile(filename):
    f=open(filename,'w')
    f.write(data)
    print("File is created and data is written\n To search a word")
    return
filename=str(input("enter file name "))
data=str(input("enter data to store "))
createfile(filename)
def wordcount(filename,word):
    with open(filename,'r')as f:
        if f.mode=='r':
            x=f.read()
            li=x.split() # It splits the string with white spaces
    cnt=li.count(word)
    return cnt
m=str(input("enter file name "))
n=str(input("enter a word "))
wordcount(m,n)


# In[ ]:




