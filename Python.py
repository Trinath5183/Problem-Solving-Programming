#!/usr/bin/env python
# coding: utf-8

# # Mark
# ## Mark
# ### Mark

# # Trinath
# ## Trinath
# ### Trinath
# #### Trinath
# ##### Trinath

# * point *

# ** point **

# **point**

# ***point***

# * krunker --[2]:https://krunker.io/?game=SIN:3609r

# * Google Site -- [Google][1]
# [1]:http://www.google.com

# * Krunker - [Krunker][2]
# [2]:https://krunker.io/?game=SIN:3609r

# In[12]:


print("hello world")


# In[13]:


print("show",end=" ")
print("man")


# In[17]:


print("trinath"," hi",end=" ")
print("kodi",end=" trinath ")
print("paanch")


# In[20]:


a=20 #single variable assignment
b=c=v=61 # multi variable assignment with same value
z,d,f=20,30,11 # multi variable assignment with different variables & values
print(a)
print(b,c,v)
print(z,f,d)


# In[24]:


x=48
y=33.48
print(x,y)
print(type(a))
print(type(y))


# In[25]:


x=48
y=33.48
print(x,y)
print(type(x),type(y))


# In[26]:


print("hello!\nhello")


# In[5]:


i=100
print(type(i))
x=str(i) # str() converts the input to string type
print(type(x))
y=float(i) # float() converts the input into float type
print(type(y))


# In[ ]:


x="100"
print(type(x))
a=int(x)
print(type(a))
f=3.3
z=int(f)
print(type(z))
print(z)


# In[7]:


#TO FIND LENGTH
a=3348
print(len(str(a)))


# In[8]:


s1=input("enter your name")
print(s1)
print(type(s1))


# # Operators

# ## Arithetic Operators

# * +
# * -
# * /
# * %
# * *
# * // # double division gives answer in int type while single division gives output in float
# ### **

# In[9]:


x,y=48,33
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x//y)
print(x**y)


# In[10]:


x=1+2**3/4+5
print(x)
print(type(x))


# ## Relational Operators
# 
# * ==
# * !=
# * greater than (>)
# * less than (<)
# * greater than or equal to (>=)
# * lessthan or equal to (<=)
# 

# In[11]:


a,b=5,8
x=(a>5 and b>8)
y=(a<6 and b<9)
print(x)
print(y)


# # Else If Syntax

# if<>:
# else:
# 
# ## or
# 
# if<>:
# elif<>:

# In[2]:


# To check given number is even or odd
n=int(input("enter a number"))
if n%2 == 0:
    print("even")
else:
    print("odd")


# In[3]:


# Given number is divisible by both 3 & 5 or not
n=int(input("enter a number"))
if n%3==0 and n%5==0:
    print("divisible by 3 & 5")
else:
    print("not divisible by 3 & 5")


# In[ ]:


# Given number is 0 or -ve or +ve
n=int(input("enter a number"))
if n==0:
    print("n=0")
elif n>0:
    print("n>0")
else:
    print("n<0")


# In[ ]:


# Largest among the three numberws
a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
if a<b and a<c:
    print(a, "is largest")
elif b<a and b<c:
    print(b,"is largest")
else:
    print(c,"is largest")


# In[ ]:


#to check given year is leap or not
n=int(input("enter a year"))
if n%4==0:
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")


# # Iterations
# 
#     1. While
#     2. For

# ## While Boolean Condition:
#       Statements
#       Increment/Decrement(update)
#       
# ### Syntax
#      while condition:
#      statements
#      update

# In[1]:


# To print A name 5 times
n=str(input("enter a name"))
i=0
while i<5:
    print(n)
    i=i+1


# In[10]:


# T print 1 to n numbers
n=int(input("enter n"))
i=0
while i<=n:
    print(i,end=" ")
    i=i+1


# In[6]:


# To read even number between 1 to n and sum them
n=int(input("enter a number"))
i=0
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1   
print(sum)


# In[7]:


# To read odd numbers  between 1 to n
n=int(input("enter a number"))
i=0
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1   
print(sum)


# In[7]:


# to print digits in given number
n=int(input("enter a number"))
r=0
print(n)
while n>0:
    r=n%10
    print(r)
    n=int(n/10)


# # Functional Programing
# 
# ## Simple
# ## Easy to read
# ## Lengthy program divides into sub-program

# ### def  name of the function (parameters):
#     Statements
#     return

# In[37]:


# Sum of even digits using functions
def addevendigits(n):
    sum=0
    while n!=0:
        r=n%10
        if r%2==0:
            sum=sum+r
        n=n//10
    return(sum)#instead of return print can also be used
n=int(input("enter a number"))
addevendigits(n)


# In[30]:


# To print Large digit in a number
def larger(n):
    a=0
    while n!=0:
        r=n%10
        if r>a:
            a=r
        n=n//10
    print(a)      
n=int(input("enter a number"))
larger(n)


# In[38]:


#To reverse a number
def reverse(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return(s)
n=int(input("enter a number"))
reverse(n)


# In[47]:


#Given number is palindrome or not
def pallindrome(n):
    s=0
    k=n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        print("pallindrome")
    else:
        return "Not a Pallindrome"
n=int(input("enter a number"))
pallindrome(n)


# In[3]:


#factorial

n=int(input("enter a number"))
def fact(n):
    f=1
    i=1
    while i<=n:
        f=f*i
        i=i+1
    return(f)
print(fact(n))


# ## Functions using for loop

# In[4]:


#To print 1 to n numbers
def num(n):
    for i in range (1,n+1):
        print(i,end=" ")
n=int(input("enter n"))
num(n)


# In[8]:


# to print alternative numbers
def num(n,m):
    for i in range (n,m-1,-1):
        print(i,end=" ")
n=int(input("enter n"))
m=int(input("enter m"))
num(n,m)


# In[1]:


for i in range(10,20-1,4):
      print(i)


# In[5]:


#to find factors of given number
def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
n=int(input("enter n"))
fact(n)


# In[7]:


# prime or not
def isprime(n):
    f=True
    for i in range (2,n//2+1):
        if n%i==0:
            f=False
            return f
        return f
n=int(input("enter n"))
isprime(n)
        


# In[22]:


# prime numbers count in 1 to n
def count(n):
    x=0
    for a in range (2,n+1):
        c=0
        for i in range (2,a//2+1):
            if a%i==0:
                c=c+1
        if c==0:
                x=x+1
    return(x)
n=int(input("enter n"))
count(n)


# In[29]:


# tp print series 1! + 2! + 31...n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[30]:


# count pallindrome
def ispallindrome(n):
    s=0
    a=n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if a==s:
        return True
    else:
        return False
def count(lb,ub):
    c=0
    while lb<=ub:
        if ispallindrome(lb)==True:
            c=c+1
        lb=lb+1
    return c
lb=int(input("enter lb "))
ub=int(input("enter ub "))        
count(lb,ub)


# In[ ]:


# Function to generate perfect numbers in a given range
def fact(n):
    a=n
    c=0
    for x in range (1,a+1):
        s=0
        i=1
        while i<x:
            if x%i==0:
                s=s+i
                x=x+1
        if s==x:
            return c  
n=int(input("enter n"))
fact(n)


# In[2]:


# Function to generate perfect numbers in given range
def fact(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s=s+i
    return s
def isperfect(n):
    if fact(n) == n:
        return True
    return False
def generatePerfect(lb,ub):
    for x in range(lb,ub+1):
        if isperfect(x):
            print(x,end=" ")
    print()
    return
generatePerfect(1,10000)


# ## Strings

# In[3]:


s='Showman'
print(s[0])           # first character
print(s[1])
print(s[len(s)-1])   #last character


# ##### Access the first character-- print(s[0:2]) or print(s[:2])
# #### Access the last three characters --print(s[-3:])
# #### To print all characters except 1st and last-- print(s[1:-1])
# #### Reverse of string --print(s[-1::-1]) or [::-1]
# #### last 2 chars in reverse order-- print(s[-1:-3:-1])
# ## Alternate characters
# #### for 2 -- print(s[::2])
# #### for 3 --print(s[::3])

# In[7]:


#reverse a string
def strrev(str):
    return str[::-1]
strrev("rogu")


# In[9]:


# String palindrome
def ispalindrome(s):
    if s==s[::]:
        return True
    else:
        return False
s=str(input("enter a sting "))
ispalindrome(s)


# ### ASCII:
# 
# * A - Z : 65 - 90
# * a - z : 97 - 122
# * 0 - 9 : 48 - 57
# * space : 32

# In[2]:


# print upper case char
def upper(s):
    for i in range (len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            print(s[i],end=" ")
s=str(input("enter a string"))
upper(s)


# In[8]:


# Function to print "Python" if the count of upper and lower
# case chars is same
# Print programming if not same
def uplo(s):
    a,b=0,0
    for i in range (len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            a+=1
        elif ord(s[i])>=97 and ord(s[i])<=122:
            b+=1
    if a==b:
        print("Python")
    else:
        print("programming")
s=str(input("enter a string"))
uplo(s)


# In[10]:


# Extract numbers from given string
def extract(s):
    for i in range (len(s)):
        if ord(s[i])>=48 and ord(s[i])<=57:
            print(s[i],end=" ")
s=str(input("enter a string"))
extract(s)


# In[19]:


# Extract numbers from given string and add
def extract(s):
    a=0
    for i in range (len(s)):
        if ord(s[i])>=48 and ord(s[i])<=57:
            a=ord(s[i])-48 + a
    print("sum of digits is",a)
s=str(input("enter a string"))
extract(s)


# In[21]:


# to count characters count differently
def word(s):
    spaceCnt=0
    for i in range (len(s)):
        if ord(s[i])==32:
            spaceCnt+=1
        if spaceCnt==1:
            if ord(s[i])>=65 and ord(s[i])<=90:
                print(s[i],end=" ")
            elif ord(s[i])>=97 and ord(s[i])<=122:
                print(chr(ord(s[i])-32),end=" ")
        if spaceCnt==2:
            break
    return
word('Python Made Easy')        
            


# In[23]:


x='gitam engineering college'
print(x[len(x)::-5])


# In[ ]:




