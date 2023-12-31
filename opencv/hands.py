import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)
hand=mp.solutions.hands
Hands=hand.Hands()
Draw=mp.solutions.drawing_utils


while True:
    ret,img=video.read()
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=Hands.process(rgb)
    points=result.multi_hand_landmarks
    h,w,l=img.shape
    lista=[]
    lista_status=[]
    dedao=4
    dados=[8,12,16,20]
    if points:
        for ponto in points:
           
           
            for ids,cord in enumerate(ponto.landmark):
                                lista.append(cord)
            for tips in dados:
                 cx,cy=int(lista[tips].x*w),int(lista[tips].y*h)
                 cv2.circle(img,(cx,cy),15,(200,245,60),cv2.FILLED)
                 if lista[tips].x <lista[tips-3].x:
                     cv2.circle(img,(cx,cy),15,(50,25,60),cv2.FILLED)
                     lista_status.append(True)
                 else:
                     lista_status.append(False)
            print(lista_status)
            if lista[dedao].y<lista[dedao-1].y<lista[dedao-2].y:
                if all(lista_status):
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,"like",(30,80), font, 5, (255,100,150), 2)
                    
            if lista[dedao].y>lista[dedao-1].y>lista[dedao-2].y:
                if all(lista_status):
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,"deslike",(30,80), font, 5, (255,10,10), 2)
                   
            Draw.draw_landmarks(img,ponto,hand.HAND_CONNECTIONS,Draw.DrawingSpec((0,0,255),2,2))

       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow("",img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
