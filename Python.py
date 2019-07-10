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


# ## Today Objectives:
# ### Python Data Structures
#          -Lists
#           -Tuples
#            -Dictionaries
# ### Basic Program sets on Data Structures
# * Advanced Problem Solving
# * Contact Application (Dictionary object) 
# ### Data Structures:
# * To store ,Search and Sort the data

# ### Python Data Structurs
# #### Lists
#  - It's one of common data structures supports by Python, the list items are seperated by comma (,) operator and enclosed in square brackets
#  * Example
#        -list1=[1,5,7,4,9]
#        -list2=["Gitam",10,45,"Hyderabad"]
#        

# In[5]:


#example "Creating the list object in python"
x=[1,4,7,9,10] 
print(x)  #access the entire term
print(x[1])   #Access the second item
print(x[-1])  #Access the last item
print(x[-2])   #Access the last to 2nd term
print(x[1:])  #Prints from second term
print(x[1:4])  #Prints from 2nd term to 4th term


# In[9]:


# Updating the list item values using index
x=[1,2,567,876]
print(x)
x[1]=440
print(x)


# In[8]:


# To delete specific item in the list
x=[1,2,567,876]
print(x)
del x[1]
print(x)


# In[12]:


#BAsic List Operators
lst=[8,4,3,0,3]
print(len(lst)) #Length of string
print(lst * 2) #Repetition
print(len(lst))
print(9 in lst) # To check whether number is present or not
print(3 in lst)
## Access the list items using iteration
for i in range (len(lst)):
    print(lst[i],end=" ")


# In[14]:


# Functions of the list
lst
print(max(lst)) # Max element in list
print(min(lst)) # Min element in list
print(sum(lst)) # Sum of all elements in the List
print(sum(lst)//len(lst)) # Gives avg of list elements
print(sum(lst[1::2])/len(lst[1::2])) # Avg of all the alternate elements


# In[46]:


lst=[1,2,3,4]
print(lst)
lst.append(83) # Adding a new element at the end of list
print(lst)
lst.insert(4,24) # Adding an element at particular index
print(lst)
lst.index(4) # Returns index value of element
lst.count(18) # Return the value how many times element repeated
print(lst.count(3))
lst.sort() # Sort the elements in ascending order
lst.pop # Remove the last element from list
print(lst)
lst.pop(1) # Remove an element from a particular index
print(lst)
lst1=[9,8,0]
lst.extend(lst1) # Merge the list2 with list1
print(lst)
lst.reverse() # Reverses the list
lst.remove(1) # Removes the list
lst.remove(3) # Removes that element
print(lst)


# In[35]:


x=[1,2,3,4,5]
print(x[-1::-3])


# In[47]:


# Function to find the second large item from the list
def seclarge(x):
    x.sort()
    return x[-2]
x=[1,2,6,3,8]
seclarge(x)


# In[50]:


# Generic Large
def genericlarge(x,n):
    x.sort()
    return x[-n]
x=[7,3,90,3,45,76]
genericlarge(x,4)


# In[52]:


# Second least in the list
def secleast(x):
    x.sort()
    return x[1]
x=[1,9,2,6,3,8]
secleast(x)


# In[53]:


# Generic Least
def genericleast(x,n):
    x.sort()
    return x[n]
x=[7,3,90,3,45,76]
genericleast(x,3)


# ### Searching Algorithm
# #### Linear Search
# #### Binary Search
# 
# ### Linear Search
# * Linear search algorithm can be applied on Duplicate and Unique List
#     - Unique list: All items of the list is appeared only once
#     - Duplicate List: The items of the list can be appeared more than once
# * Linear search algorithm can applied on Sorted and unsorted data

# In[3]:


# Function to search the data in a list
# Search is found then return the index <if not return -1
def linearsearch(x,target):
    for i in range(len(x)):
        if x[i]==target:
            return i
    return -1
x=[5,8,3,4,8]
linearsearch(x,9)


# In[7]:


# Function 
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearSearch(x,target):
    for i in range (len(x)):
        if x[i]==target:
            print(i,end=" ")
    return
x=[1,5,9,6,5,15,1,2,5]
linearSearch(x,5)


# In[15]:


# Function
#input : list
# Output : Seq of characters
# Test case
#[1,5,9,6,15,1,2,5],target=5 -- # 1 4 8== !! !!!!! !!!!!!!!!
def linearSearch(x,target):
    for i in range (len(x)):
        if x[i]==target:
            for a in range (1,i+2):
                print("!",end=" ")
            print(end=" ")
    return
x=[1,5,9,6,5,15,1,2,5]
linearSearch(x,5)


# In[20]:


# Function
# Input : List
# output : Formatted
# Test case :
# [12,2,45,9,18,15,36] -- 60
# A list item which is perfect multiples of 3 & 5
def linearsearch(x):
    s=0
    for i in range (len(x)):
        if  x[i]%3 ==0 and x[i]%5==0:
            s=s+x[i]
    return s
x=[12,2,45,9,18,15,36]
linearsearch(x)


# In[33]:


#Function
# Input : List
# Output : Formated Output
# Test Case:
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def plot(x):
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            print(x[i],end=" ")
        else:
            print(x[i-1] * x[i+1],end=" ")
    return
x=[1,2,3,4,5]
plot(x)     


# In[36]:


# Function 
# Input : List
# Output : Formated Output
# Test Case:
#[1,6,9,4,16,19,22] -- 1 9 19 22 (If element is surrounded by even numbers print)
def plot(x):
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            print(x[i],end=" ")
        elif x[i-1]%2==0 and x[i+1]%2==0:
            print(x[i],end=" ")
    return
x=[1,6,9,4,16,19,22]
plot(x)


# ### Number to List
# * Input as Number
# * Expected Output will be list

# In[51]:


# Function for convertion __ Number to list
# Input -- Number
# Output -- list
# Test case :
#14569 -- [1,4,5,6,9]
#1990 -- [1,9,9,0]
def convert(n):
    i=1
    s=[]
    while n!=0:
        r=n%10
        s.append(r)
        n=n//10
        i=i+1
    s.reverse()
    return s 
n=int(input("enter a number"))
convert(n)


# In[61]:


#*** Function to count the occurances of a character in a string
def repeat(x,target):
    c=0
    for i in x:
        if i==target:
            c+=1
    return c
# (OR)
#def repeat1(x,target):
#    return x.count(target)
n=str(input("enter a string-"))
m=str(input("enter target element-"))
repeat(n,m) 


# In[65]:


# Function to convert string to list
# Test case:
# "1 2 3 4 5 6"--[1,2,3,4,5,6]
def convert(s):
    x=s.split() # Splits the string
    numlist=[]
    for i in x:
        numlist.append(int(i))
    return numlist
s='1 2 3 4 5 6'
convert(s)


# ## Sorting Algorithm
#   * All the sorting algorithms makes the list into ascending order
#      - Bubble Sort
#      - Selection Sort
#      - Insertion Sort

# ### Bubble Sort
# * This algorithm compares the adjacent elements, if the first element is greater than second element then its required to swap the elements

# In[70]:


# Function to represent the Bubble Sort
def bubbleSort(s):
    for j in range(len(s)-1):
        for i in range (len(s)-1):
            if s[i] > s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
    return s
s=[24,46,25,532]
bubbleSort(s)


# ### Dictionaries
# * It works on the concept of Set Unique Data
# * Keys , Values is the unique identifier for a value
# * Each key is seperated fron its values with colon (:)
# * Each key and value is seperated by comma (,)
# * Dictionaries enclosed with curly braces "{}"

# In[7]:


# exanple:
d={"Name":"Eraser","Interest":"Racing","Do":"Race"}
print(d)


# In[3]:


d["Name"]


# In[5]:


d["Interest"]="Bike Racing"


# In[6]:


d["Interest"]


# In[10]:


del d["DO"]


# In[12]:


del d["Do"]


# In[14]:


d # del d --will delete the entire dictionary object


# In[15]:


d.keys() # Returns the list of keys


# In[16]:


d.values() # Returns the values


# In[18]:


d.items() # Returns the list of tuples of keys & values


# ### Tuples
# * t1 parenthesis() li square brackets[]
# * Difference between Tuple and List
#     - lists are mutable - can be changed/modified
#             * Used to access modify,Add, Delete data
#     - Tuples are immutable - cannot be changed
#             * Used to data only

# ### Contact Application
# * Add Contact
# * Search the Contact
# * List all contacts
#      - name1 : phone1
#      - name2 : phone2
# * Modify the contact
# * Remove the contact
# * Import the contact

# In[24]:


# Add Contact
contact={}   # Creating a dictionary object
def addcontact(name,phone):
    if name not in contact:
        contact[name]=phone
        print("Contact details are added")
    else:
        print("Contact Details already exists")
    return
addcontact('vamshi','9052780366')
addcontact('Someone','9553754259')
addcontact('vamshi','9052780366')
addcontact('rascal','9052780366')


# In[28]:


# To search for contact details
def searchContact(name):
    if name in contact:
        print(name,":",contact[name])
    else:
            print("%s does not exists" % name)
    return
searchContact('vamshi')
searchContact('rowdy')


# In[45]:


# Import some contacts
# Merge wiyh existing one
def importcontact(newContact):
    contact.update(newContact)
    print(len(newContact.keys()),"Contact added succesfully")
    return
newContact={'Dinesh':453698369,'rock':563249667}
importcontact(newContact)
contact


# In[46]:


# Delete a contact:
def delete(name):
    if name in contact:
        del contact[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
delete("Dinesh")
contact


# In[47]:


# Updating contact details:
def update(name,phone):
    if name in contact:
        contact[name]=phone
        print(name,"Updated successfully")
    else:
        print(name,"Not Exists")
    return
update('rock',46646384)
update('rowdy',74675682)
contact


# ### String functions
# * upper() - Will converts the given string into upper case
# * lower() - Will converts the given string into lower case

# In[49]:


s='giTam'
print(s.upper())
print(s.lower())


# ### Boolean Function (True / False)
# * islower() -- True if the string is in lower case  / False if the string not in lower
# * isupper() -- True if the string is in upper case  / False if the string not in upper

# In[51]:


s='gitam'
print(s.islower())
print(s.isupper())


# In[52]:


s1='Python Programming'
s2='python Programming'
print(s1.istitle())
print(s2.istitle())


# In[53]:


s1='Application23435'
s2='PythonProgramming'
print(s1.isalpha())
print(s2.isalpha())


# In[54]:


s1=" "
s2="py u yh"
print(s1.isspace())
print(s2.isspace())


# In[55]:


s1='Python'
print(" ".join(s1))


# In[56]:


s=['python','some','shoot']
print(",".join(s))


# ### String Methods
# * join()
# * split()
# * replace() -- replaces a word or anything

# In[58]:


s1="pyton program done"
print(s1.split())


# In[59]:


li=s1.split()
print(li)
print(len(li))


# In[60]:


s1="pyton program done"
li=list(s1)
print(li)


# In[61]:


s2='python programming'
print(s2.replace('pro','PRO'))


# In[62]:


# import external packages to python files
import math
math.floor(123.456)


# In[63]:


from math import factorial as fact
fact(4)


# In[ ]:




