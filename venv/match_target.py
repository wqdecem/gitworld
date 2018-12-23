#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class MatchTarget(object):
    """description of class"""

    def __init__(self):
        pass

    def match_target(self, template_path, target_path,show_method = 'img'):
        
        img = cv.imread(target_path,0)

        img2 = img.copy() # copy,才会获取新的Mat,clone()和直接赋值都会导致共享数据区,也就是相当于&

        template = cv.imread(template_path,0)
        w, h = template.shape[::-1]
        # All the 6 methods for comparison in a list
        #methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
        #            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        # cv::TM_SQDIFF：该方法使用平方差进行匹配，因此最佳的匹配结果在结果为0处，值越大匹配结果越差
        # cv::TM_SQDIFF_NORMED：该方法使用归一化的平方差进行匹配，最佳匹配也在结果为0处
        # cv::TM_CCORR：相关性匹配方法，该方法使用源图像与模板图像的卷积结果进行匹配，因此，最佳匹配位置在值最大处，值越小匹配结果越差
        # cv::TM_CCORR_NORMED：归一化的相关性匹配方法，与相关性匹配方法类似，最佳匹配位置也是在值最大处
        # cv::TM_CCOEFF：相关性系数匹配方法，该方法使用源图像与其均值的差、模板与其均值的差二者之间的相关性进行匹配，最佳匹配结果在值等于1处，最差匹配结果在值等于-1处，值等于0直接表示二者不相关
        # cv::TM_CCOEFF_NORMED：归一化的相关性系数匹配方法，正值表示匹配的结果较好，负值则表示匹配的效果较差，也是值越大，匹配效果也好
        methods = ['cv.TM_CCOEFF']
        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res) # 该函数不仅可以同时获取到cv::Mat中的最大和最小值，而且还可以获得最大最小值所在的位置
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            
            cv.rectangle(img,top_left, bottom_right, 255, 2)
            plt.subplot(121)#把绘图区域等分为1行*2列共2个区域, 然后在区域1(左区域)中创建一个轴对象. 
            plt.imshow(res,cmap = 'gray')

            # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.title('Matching Result'), 
            plt.xticks([]), plt.yticks([]) # 去除坐标的显示
            plt.subplot(122),plt.imshow(img,cmap = 'gray')

            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            if show_method == 'img':
                img = cv.imread(target_path,1)
                cv.rectangle(img,top_left, bottom_right, 255, 2)
                cv.imshow('target',img)
                wait_key = cv.waitKey(0)
                if wait_key == 27:         # wait for ESC key to exit
                    cv.destroyAllWindows()
                elif wait_key == ord('s'): # wait for 's' key to save and exit
                    cv.imwrite('messigray.png',img)
                    cv.destroyAllWindows()
            else:
                plt.show()

if __name__ == '__main__':
    T = MatchTarget()
    T.match_target(r'D:\mat\template.png',r'D:\mat\image3000.png',show_method ='img')




