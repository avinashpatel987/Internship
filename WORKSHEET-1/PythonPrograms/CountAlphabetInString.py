#!/usr/bin/env python
# coding: utf-8

# In[2]:


string = input("Enter a string:")
freq = {}
  
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
print (str(freq))

