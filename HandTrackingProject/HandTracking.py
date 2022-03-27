import cv2
import mediapipe as mp

def listappender(xyztext,xyzlist):
    for i in xyztext:
        xyzlist.append(float(i[:-1]))

x1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/x1.txt","r")
y1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/y1.txt","r")
z1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/z1.txt","r")

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

yazi = " "
xortlist = []
yortlist = []
zortlist = []

listappender(x1listesi,xortlist)
listappender(y1listesi,yortlist)
listappender(z1listesi,zortlist)
while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        a = results.multi_hand_landmarks
        q = a[0].landmark
        count1 = 0
        count_last,count_last1,count_last2 = 0,0,0
        for j in q:
            de = (str(j)).split("\n")
            x0 = float(de[0][3:])
            y0 = float(de[1][3:])
            z0 = float(de[2][3:])
            x01 = (xortlist[count1] * 8) / 10
            y01 = (yortlist[count1] * 8) / 10
            z01 = (zortlist[count1] * 8) / 10

            x02 = (xortlist[count1] * 12) / 10
            y02 = (yortlist[count1] * 12) / 10
            z02 = (zortlist[count1] * 12) / 10

            if x0 >= x01 and x0 <= x02:
                count_last+=1

            if y0 >= y01 and y0 <= y02:
                count_last1+=1

            if z0 <= z01 and z0 >= z02:
                count_last2+=1

            count1 += 1
        if count_last1 >= 21 and count_last2 >= 0 and count_last>= 0:
            if True:
                yazi = "NAH CEKME OC"
                cv2.putText(img, yazi, (150, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255),
                            2)



        print(count_last)
    else:
        if yazi != "AFFERIM LEN":
            yazi = "AFFERIM LEN"
            print(yazi)


    cv2.imshow("Image", img)
    cv2.waitKey(1)

x1listesi.close()
y1listesi.close()
z1listesi.close()
