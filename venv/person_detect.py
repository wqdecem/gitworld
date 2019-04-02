#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

#use hog
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
img = cv2.imread(r'C:\Users\Administrator\Desktop\2.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
person_hog = hog.detectMultiScale(gray,winStride=(4,4),padding=(32, 32),scale=1.05)
# winStride window stride
# padding object padding
# scale image pyramid scale
img_hog = img.copy()
for i in range(len(person_hog[0])):
    if person_hog[1][i]==max(person_hog[1]):
        (x,y,w,h) = person_hog[0][i]

        img_hog = cv2.putText(img_hog,'%s' % person_hog[1][i],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
        img_hog = cv2.rectangle(img_hog,(x,y),(x+w,y+h),(255,0,0),1)

cv2.imshow('img_hog',img_hog)

#use haar cascade
person_cascade = cv2.CascadeClassifier(r'D:\python36\Lib\site-packages\opencv\python\sources\data\haarcascades\haarcascade_upperbody.xml')
person_cascade = person_cascade.detectMultiScale(gray,1.05,3)
img_haar = img.copy()
for (x,y,w,h) in person_cascade:

    img_haar = cv2.rectangle(img_haar,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img_haar',img_haar)

cv2.waitKey(0)
cv2.destroyAllWindows()

