#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np


class BasicOperate(object):
    def __init__(self):

        print("Do noting")

    def read_img(self,path,color=True):
        # 彩色模式、灰度图模式 cv2.IMREAD_COLOR =1, cv2.IMREAD_GRAYSCALE =0
        if color:
            img = cv2.imread(path, cv2.IMREAD_COLOR)
        else:
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        return img

    def resize_window(self,window_name, x_coordinate, y_coordinate):
        # resize window
        cv2.resizeWindow(window_name, x_coordinate, y_coordinate)

    def set_osd(self,img,word,position=(0,0),fonttype =3,fontzise=1,colors=(0,0,0),fontweight=2):

        cv2.putText(img, word, position, fonttype, fontzise, colors,fontweight)

    def show_window(self,img,window_name):

        cv2.imshow(window_name, img)  # Show the image


    def resize_img(self,img,shape,interpolation = cv2.INTER_CUBIC):
        # interpolation 插值法：缩小时用INTER_AREA，扩大时用INTER_CUBIC或者INTER_LINEAR(更快)
        return cv2.resize(img, shape, interpolation=interpolation)

    def rotate_img_matrix(self,heart_pos,angle=0,zoom=1):

        matrix = cv2.getRotationMatrix2D(heart_pos, angle, zoom)
        # 得到变换的矩阵，通过这个矩阵再利用warpAffine来进行变换
        # 第一个参数就是旋转中心，元组的形式，这里设置成相片中心
        # 第二个参数90，是旋转的角度
        # 第三个参数1，表示放缩的系数，1表示保持原图大小
        return matrix

    def transfer_img_3dmatirx(self,ori_points, tar_poins):
        ##################### 对图像进行变换（三点得到一个变换矩阵）
        # 我们知道三点确定一个平面，我们也可以通过确定三个点的关系来得到转换矩阵
        # points1 = np.float32([[1, 0], [2, 0], [0, 1]])
        # points2 = np.float32([[2, 0], [4, 0], [0, 2]])
        matrix = cv2.getAffineTransform(ori_points, tar_poins)
        return matrix

    def transfer_img(self,img,matrix,shape):

        return cv2.warpAffine(img, matrix, shape)

    def create_img(self,shape,dtype):
        #dtype=np.uint8
        img = np.zeros(shape, dtype=dtype)
        return img

    def change_color_space(self,img,type):
        #函数实现图片颜色空间的转换，flag 参数决定变换类型。
        #BGR->Gray flag 就可以设置为 cv2.COLOR_BGR2GRAY
        #COLOR_BGR2YCrCb
        #COLOR_BGR2HSV
        #COLOR_YCrCb2BGR
        return cv2.cvtColor(img, type)

    def set_img_to_single_color(self,img,color="blue"):
        B, G, R = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        if color=="blue":
            return cv2.merge([B, zeros, zeros])
        elif color=="green":
            return cv2.merge([zeros, G, zeros])
        elif color=="red":
            return cv2.merge([zeros, zeros, R])

    def capture_video(self, interval=1, num=1):
        cap = cv2.VideoCapture(r'D:\downloads\Secret.2007.1080p.Bluray.x264-aBD\abd-secret.mkv')
        count = 1
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            print(count)
            if (count%interval==0):
                print('############')
                cv2.imwrite(r'D:\mat\image%s.png' % count,frame,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            # cv2.imshow('frame', gray)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            if count%(num*interval)==0:
                break
            count += 1
        # When everything done, release the capture
        cap.release()

path =r'C:\Users\Administrator\Desktop\KYXR7342.jpg'
BO = BasicOperate()
img = BO.read_img(path,color=False)
h,w =img.shape[:2]
BO.set_osd(img,"Hello World!",position=(int(w/2),int(h/2)))

newone = BO.resize_img(img,shape=(2*w,2*h))
BO.show_window(newone,"2x")
'''
M = BO.rotate_img_matrix(heart_pos=(w/2,h/2),angle=180)
newtwo = BO.transfer_img(img,M,shape=(w,h))
#BO.show_window(newtwo,"left")

M = BO.rotate_img_matrix(heart_pos=(0,h),angle=270,zoom=1)
newtwo1 = BO.transfer_img(img,M,shape=(2*w,2*h))
#BO.show_window(newtwo1,"left2")

pos1=np.float32([[1, 0], [2, 0], [0, 1]])
pos2=np.float32([[2, 0], [4, 0], [0, 2]])
M=BO.transfer_img_3dmatirx(pos1,pos2)
newtwo2 = BO.transfer_img(img,M,shape=(2*w,2*h))

#BO.show_window(newtwo2,"left3")

img2 = BO.create_img(img.shape,dtype=np.uint32)

img2 = BO.change_color_space(img,cv2.COLOR_BGR2HSV)
#BO.show_window(img2,"COLOR_BGR2HSV")
img2 = BO.change_color_space(img,cv2.COLOR_BGR2YCrCb)
#BO.show_window(img2,"COLOR_BGR2YCR_CB")
#img2 = BO.change_color_space(img,cv2.COLOR_BGR2GRAY)

#BO.show_window(img2,"COLOR_BGR2GRAY")
print(img2.dtype)

B,G,R =cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype="uint8")
Y=zeros
U=zeros
V=zeros
#for width in range(len(R)):
#    for heigh in range(len(R[1])):
#        Y[width][heigh]=(int(0.30*R[width][heigh]+0.59*G[width][heigh]+0.11*B[width][heigh]))
#for width in range(len(R)):
#    for heigh in range(len(R[1])):
#        U[width][heigh]=(int(0.493*(B[width][heigh]-Y[width][heigh])))
#        V[width][heigh]=(int(0.877*(R[width][heigh]-Y[width][heigh])))


zeros = np.zeros(img.shape[:2], dtype="uint8")

img3 = BO.set_img_to_single_color(img,color="red")
#BO.show_window(img3,"img3")

img4 =cv2.merge([B, G,R])
#BO.show_window(img4,"img4")
BO.capture_video(interval=250,num=100)'''
wait_key = cv2.waitKey(0)
if wait_key == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif wait_key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
