#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os

class Training(object):

    def __init__(self):
        self.origin_img_path = r'D:\downloads\3\opencv\build\x64\vc11\bin\posdata'
        self.target_img_path = r'D:\downloads\3\opencv\build\x64\vc11\bin\posdata\tar'

    def resize_img(self,ori_path,tar_path):
        files = os.listdir(ori_path) #得到文件夹下的所有文件名称
        if not os.path.exists(tar_path):
            os.makedirs(tar_path)
        for file in files:  # 遍历文件夹
            if 'png' in file:
                temp_path = '%s\\%s' % (ori_path,file)

                img = cv2.imread(temp_path, cv2.IMREAD_GRAYSCALE)
                # h, w = img.shape[:2]
                tar_img = cv2.resize(img, (352,288), interpolation=cv2.INTER_AREA)
                cv2.imwrite('%s\\%s' % (tar_path,file), tar_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

T = Training()
origin_img_path = r'D:\mat\negdata'
target_img_path = r'D:\mat\negdata\tar'
T.resize_img(origin_img_path,target_img_path)
