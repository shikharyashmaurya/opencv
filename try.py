import cv2
import numpy as np

# reading an image
img=cv2.imread('opencv/bird.png')
img=cv2.resize(img,(400,400))
temp=img.copy()
cv2.imshow('image',img)
cv2.waitKey(0)

# converting
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img_gray)
cv2.waitKey(0)

# saving image
# cv2.imwrite('opencv/bird2.png',img_gray)

# rgb
img=temp.copy()
img[:,:,0]=0
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
img[:,:,1]=0
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
img[:,:,2]=0
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
stackedimg=np.hstack((img[:,:,0],img[:,:,1],img[:,:,2]))
cv2.imshow('image',stackedimg)
cv2.waitKey(0)

img=temp.copy()
img=cv2.flip(img,0)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
img=cv2.flip(img,1)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
img=cv2.flip(img,-1)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
cv2.imshow('image',img[100:300,100:300])
cv2.waitKey(0)

img=temp.copy()
cv2.rectangle(img,(100,100),(300,300),(255,0,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
cv2.circle(img,(100,100),50,(255,0,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
cv2.line(img,(100,100),(300,300),(255,0,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)

img=temp.copy()
cv2.putText(img,org=(100,100),text='Hello',fontScale=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,color=(255,0,0),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)