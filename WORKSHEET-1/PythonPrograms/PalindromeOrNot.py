#!/usr/bin/env python
# coding: utf-8

# In[33]:


def isPalindrome(s):
    return s == s[::-1]

s = input("Enter A string:")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")  

