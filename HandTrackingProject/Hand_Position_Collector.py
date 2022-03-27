import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
liste = []
a  = ""
frames = 750
xlistesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/x.txt","w")
ylistesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/y.txt","w")
zlistesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/z.txt","w")

count = 0
while count < frames:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        a = results.multi_hand_landmarks
        count += 1
        liste.append(a[0].landmark)
        q = a[0].landmark

    cv2.putText(img, f"{count} Frames Saved", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (215, 5, 5), 2)
    cv2.putText(img, f"{frames-count} Frames Remaining", (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 5, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

for i in liste:
    for j in i:
        q = (str(j)).split("\n")
        xlistesi.write(q[0][3:]+"\n")
        ylistesi.write(q[1][3:] + "\n")
        zlistesi.write(q[2][3:] + "\n")

xlistesi.close()
ylistesi.close()
zlistesi.close()