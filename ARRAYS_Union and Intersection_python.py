#!/usr/bin/env python
# coding: utf-8

# # Question:
# ## Union and Intersection of two sorted arrays
# Given two sorted arrays, find their union and intersection.
# Example:
# 
# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6} 
# Output : Union : {1, 2, 3, 4, 5, 6, 7} 
#          Intersection : {3, 5}
# 
# Input : arr1[] = {2, 5, 6}
#         arr2[] = {4, 6, 8, 10} 
# Output : Union : {2, 4, 5, 6, 8, 10} 
#          Intersection : {6}

# In[1]:


#Taking input
arr1=[int(i) for i in input("Enter values of arr1: ").split()]
arr2=[int(i) for i in input("Enter values of arr2: ").split()]
arr3=[]


# In[2]:


m=len(arr1)
n=len(arr2)


# In[3]:


#Union of two arrays
for i in range(m):
    if arr1[i] not in arr3:
         arr3.append(arr1[i])        

for i in range(n):
    if arr2[i] not in arr3:
        arr3.append(arr2[i])
print("Union of arr1 and arr2:",arr3)



# In[4]:


#Intersection of two arrays
arr4=[lambda x: x in arr1,arr2]
print("Intersection of arr1 and arr2: ",arr4)


# In[ ]:




