import cv2
import mediapipe as mp
import funcs_last_last
import numpy as np
commandsX = ["fourfingersX1","fourfingersX2","fourfingersX3","fivefingersX1","fivefingersX2","fivefingersX3"]
commandsY = ["fourfingersY1","fourfingersY2","fourfingersY3","fivefingersY1","fivefingersY2","fivefingersY3"]
commandsZ = ["fourfingersZ1","fourfingersZ2","fourfingersZ3","fivefingersZ1","fivefingersZ2","fivefingersZ3"]

xortlist = []
yortlist = []
zortlist = []
xeq1_list = []
yeq1_list = []
zeq1_list = []

for i in range(len(commandsX)):
    x8 = commandsX[i]
    y8 = commandsY[i]
    z8 = commandsZ[i]
    x1listesi = open(f"D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/{x8}.txt", "r")
    y1listesi = open(f"D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/{y8}.txt", "r")
    z1listesi = open(f"D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/{z8}.txt", "r")
    xortlist.append([])
    yortlist.append([])
    zortlist.append([])
    funcs_last_last.listappender(x1listesi, xortlist)  # xort list oluşur 2 boyutlu olarak şuanda 2*21
    funcs_last_last.listappender(y1listesi, yortlist)
    funcs_last_last.listappender(z1listesi, zortlist)

    xeq1_list.append([])
    yeq1_list.append([])
    zeq1_list.append([])
    for j in range(21):
        xeq1_list[i].append([]) #xeq1_list oluşur 3 boyutlu olarak şuanda 2*21*21
        yeq1_list[i].append([])
        zeq1_list[i].append([])

funcs_last_last.listminus(xortlist,xeq1_list) #xeq1_list'i oluşturur (alınan ortalamaların farkı)  ortalama değerler için olan fark
funcs_last_last.listminus(yortlist,yeq1_list)
funcs_last_last.listminus(zortlist,zeq1_list)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

yazi = " "
count = 0
while count < 1500:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    x_current = []
    y_current = []
    z_current = []
    xeq_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    yeq_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    zeq_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    if results.multi_hand_landmarks:
        count += 1
        a = results.multi_hand_landmarks
        q = a[0].landmark
        count1 = 0
        count_last,count_last1,count_last2 = 0,0,0
        for j in q:
            de = (str(j)).split("\n")
            x0 = float(de[0][3:])
            y0 = float(de[1][3:])
            z0 = float(de[2][3:])

            x_current.append(x0)
            y_current.append(y0)
            z_current.append(z0)

        funcs_last_last.listminus_current(x_current, xeq_list)  #x_current = 21 values
        funcs_last_last.listminus_current(y_current, yeq_list)
        funcs_last_last.listminus_current(z_current, zeq_list)
        last_list = []
        for i in range(len(commandsX)):
            xWell = funcs_last_last.translator(xeq_list,xeq1_list)
            yWell = funcs_last_last.translator(yeq_list,yeq1_list)
            zWell = funcs_last_last.translator(zeq_list,zeq1_list)

            last_value = xWell[i]+yWell[i]+zWell[i]
            last_list.append(last_value)

        max_value = 0
        last_of = 99
        for i in range(len(commandsX)):
            if max_value < last_list[i]:
                max_value = last_list[i]
                last_of = i


        cv2.putText(img, commandsX[last_of], (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)


    cv2.putText(img, "__________", (160, 130), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)
    cv2.putText(img, "__________", (160, 380), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

x1listesi.close()
y1listesi.close()
z1listesi.close()