import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
liste = []
while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        a = results.multi_hand_landmarks
        liste.append(a[0].landmark)
        q = a[0].landmark
        print(type(q[0]))

    cTime = time.time()
    fps = round(1/(cTime-pTime),5)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,5,255),
                2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)