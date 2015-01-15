# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 01:15:28 2015

@author: suryo
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

i=0

while(i!=30):
    ret, frame = cap.read();
    i=i+1
    
img=frame
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def draw_circle(event,x,y,flags,param):
    
    #Double click to find the HSV value of the pixel pointed to.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print img.item(x,y,0)
        print img.item(x,y,1)
        print img.item(x,y,2)

cv2.namedWindow('image')

# mouse callback function
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
