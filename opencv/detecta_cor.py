import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


cap=cv.VideoCapture(0)
cv.namedWindow("Cor_Bar")
cv.createTrackbar("LH","Cor_Bar",0,255,nothing)
cv.createTrackbar("LS","Cor_Bar",0,255,nothing)
cv.createTrackbar("LV","Cor_Bar",0,255,nothing)
cv.createTrackbar("UH","Cor_Bar",255,255,nothing)
cv.createTrackbar("US","Cor_Bar",255,255,nothing)
cv.createTrackbar("UV","Cor_Bar",255,255,nothing)
while True:
    _, img=cap.read()
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
   
    l_h=cv.getTrackbarPos("LH","Cor_Bar")
    l_s=cv.getTrackbarPos("LS","Cor_Bar")
    l_v=cv.getTrackbarPos("LV","Cor_Bar")

    u_h=cv.getTrackbarPos("UH","Cor_Bar")
    u_s=cv.getTrackbarPos("US","Cor_Bar")
    u_v=cv.getTrackbarPos("UV","Cor_Bar")


    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(img,img,mask=mask)
  
   
    
    
    cv.imshow("img",img)
    cv.imshow("mask",mask)
    cv.imshow("res",res)

    k=cv.waitKey(1) & 0xFF
    if k==27 or k==ord('q'):
        break
        
   

cap.release()
cv.destroyAllWindows()
