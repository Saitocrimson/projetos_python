import numpy as np
import cv2 as cv


def nothing(x):
    print(x)



cv.namedWindow('ChangeColor!')
cv.createTrackbar('pos', 'ChangeColor!',0,400,nothing)
cv.createTrackbar('b', 'ChangeColor!',0,255,nothing)
cv.createTrackbar('g', 'ChangeColor!',0,255,nothing)
cv.createTrackbar('r', 'ChangeColor!',0,255,nothing)

while(1):
    img = np.zeros((300,512,3),np.uint8)    
    k=cv.waitKey(1) & 0xFF
    if k==27 or k==ord('q'):
        break
    bs = cv.getTrackbarPos('b','ChangeColor!')
    gs = cv.getTrackbarPos('g','ChangeColor!')
    rs = cv.getTrackbarPos('r','ChangeColor!')
    img[:]=[bs,gs,rs]
    if rs==255 or bs==255 or gs==255:
        cor=(0,0,0)
    else:
        cor=(0,0,255)
    font =cv.FONT_HERSHEY_SIMPLEX
    tam=cv.getTrackbarPos('pos','ChangeColor!')
    cv.putText(img,"Aperte Q ou ESC para sair",(50,150),font, 1, cor,4)
    cv.putText(img,str(tam),(50,150), font, 4, cor,1)
    
    
    cv.imshow('ChangeColor!',img)
        
   


cv.destroyAllWindows()

