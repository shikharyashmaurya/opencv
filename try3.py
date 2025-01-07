import cv2
import time

cap=cv2.VideoCapture(0)

## for using saved video
# out=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
# cap=cv2.VideoCapture('output.avi')

while True:
    
    ret,frame=cap.read()

    # out.write(frame)
    # time.sleep(1/20)

    cv2.imshow('image',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

# out.release()
cap.release()
cv2.destroyAllWindows()