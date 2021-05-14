#imports
import cv2
import mediapipe as mp
import time

#videocaptue
capture=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands =mpHands.Hands()
mpDraw= mp.solutions.drawing_utils
#ultra cool rgb frame rate text  woooowwww(the set up)

red =0
r1=False
b=0
b1=False
green=0
g1=False


#fps
pTime=0
cTime=0
#loop
while True:
    success, img=capture.read()#takes image from camrea

    #converts into RGB for hand recognition
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)  # tells location of handmarks

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            """"
            for id,lm in enumerate(handLms.landmark):#infomation on location, usful for future devolpement eg hand signals to do an action
                print(id,lm)
            """
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)#draws landmarks(red dots and greenlines)




    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    #fps display
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(red,green,b),3)
    #RGB fps code
    red=red+1
    if red==255:
        r1=True
    if r1 ==True:
        red=red-1
        b=b+1
        if b==225:
            b1=True
        if b1==True:
            red=red+1
            b=b-1
            green=green+1
        if green ==225:
            b1=False
            r1=False
            g1=False
            b=0
            red=0
            green=0
    #displays image
    cv2.imshow("Image",img)#displays camrea
    cv2.waitKey(1)#not sure but is important for the display capture to work
