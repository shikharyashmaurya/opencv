import cv2

flag=0
ix=-1
iy=-1

img=cv2.imread('opencv/bird.png')
img=cv2.resize(img,(400,400))

# drawing a circle
# def draw(event,x,y,flags,param):
#     if event==0:
#         cv2.circle(img,(x,y),10,(255,0,0),-1) 

# drawing a rectangle
def draw(event,x,y,flags,param):
    global flag,ix,iy
    if event==1:
        flag=True
        ix=x
        iy=y
    elif event==0:
        if flag==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
    elif event==4:
        flag=False
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cv2.destroyAllWindows()