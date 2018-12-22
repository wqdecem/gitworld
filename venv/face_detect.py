#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import basic_operate
BO=basic_operate.BasicOperate()
face_cascade = cv2.CascadeClassifier(r'D:\python36\Lib\site-packages\opencv\python\sources\data\lbpcascades\lbpcascade_frontalface_improved.xml')
eye_cascade = cv2.CascadeClassifier(r'D:\python36\Lib\site-packages\opencv\python\sources\data\haarcascades\haarcascade_eye.xml')
img = cv2.imread(r'C:\Users\Administrator\Desktop\KYXR7342.JPG')
h,w =img.shape[:2]
img = cv2.resize(img, (int(w/1),int(h/1)), interpolation=cv2.INTER_CUBIC)

M = BO.rotate_img_matrix(heart_pos=(w/2,h/2),angle=45)
img = BO.transfer_img(img,M,shape=(2*w,2*h))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
