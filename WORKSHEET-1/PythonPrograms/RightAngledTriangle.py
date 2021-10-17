#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
def CalcSide(a,b,c):
    if(c==1):
        side=str(math.sqrt((b**2)-(a**2))) 
        print("Your Other Side Is:"+side)
        return 0
    else:
        side=str(math.sqrt((a**2)+(b**2)))
        print("your Hypotenus Is:"+side)
        return 0
    
print("Select Your Option Which You Want To find:")
num=int(input(print("1: Either One Of The Sides \n2: hypotenus")))
if(num==1):
    side1=int(input("Enter One Side:"))
    hyp=int(input("Enter the Hypotenus:"))
    CalcSide(side1,hyp,num)
else:
    side1=int(input("Enter First Side:"))
    side2=int(input("Enter Second Side:"))
    CalcSide(side1,side2,num)


# In[ ]:





# In[ ]:




