#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[2]:


def image_pyramid(image,scale=1.5,minSize = (224,224)):
    
    yield image
    
    while True:
        w = int(image.shape[1]/scale)
        image = cv2.resize(image,dsize=(w,w))
        
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        
        yield image
        

