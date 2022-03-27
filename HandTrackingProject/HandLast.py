import cv2
import mediapipe as mp
import funcs


x1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/fuckX.txt","r")
y1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/fuckY.txt","r")
z1listesi = open("D:/Users/akif/PycharmProjects/HandTrackingProject/txtFiles/fuckZ.txt","r")

xeq_list =  [[],[],[],[],[],[],[],[],[],[],[]]
xeq1_list = [[],[],[],[],[],[],[],[],[],[],[]]
yeq_list =  [[],[],[],[],[],[],[],[],[],[],[]]
yeq1_list = [[],[],[],[],[],[],[],[],[],[],[]]
zeq_list =  [[],[],[],[],[],[],[],[],[],[],[]]
zeq1_list = [[],[],[],[],[],[],[],[],[],[],[]]

xortlist = []
yortlist = []
zortlist = []

funcs.listappender(x1listesi,xortlist)  #xort list'i oluşturur   21 HANE
funcs.listappender(y1listesi,yortlist)
funcs.listappender(z1listesi,zortlist)

funcs.listminus(xortlist,xeq1_list) #xeq1_list'i oluşturur (alınan ortalamaların farkı)  ortalama değerler için olan fark
funcs.listminus(yortlist,yeq1_list)
funcs.listminus(zortlist,zeq1_list)
print(xeq1_list)

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
    xeq_list = [[],[],[],[],[],[],[],[],[],[],[]]
    yeq_list = [[], [], [], [], [], [], [], [], [], [], []]
    zeq_list = [[], [], [], [], [], [], [], [], [], [], []]
    xdifflist_current = [[], [], [], [], [], [], [], [], [], [], []]
    ydifflist_current = [[], [], [], [], [], [], [], [], [], [], []]
    zdifflist_current = [[], [], [], [], [], [], [], [], [], [], []]

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
            """
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
        if count_last1 >= 21 :
            yazi = "NAH CEKME OC"
            cv2.putText(img, yazi, (150, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255),2)

    else:
        yazi = "NO HANDS"
        cv2.putText(img, yazi, (150, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 2)
"""
            x_current.append(x0)
            y_current.append(y0)
            z_current.append(z0)

        funcs.listminus(x_current, xeq_list)
        funcs.listminus(y_current, yeq_list)
        funcs.listminus(z_current, zeq_list)

        xWell = funcs.translator(xeq_list,xeq1_list)
        yWell = funcs.translator(yeq_list,yeq1_list)
        zWell = funcs.translator(zeq_list,zeq1_list)
        last_value = xWell*yWell*zWell

        print(last_value)

        if last_value > 300000:
            cv2.putText(img, "ORTA PARMAGININ AQ", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)
        """if last_value > 300000:
            cv2.putText(img, "NAH CEKME OC", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)
        elif last_value > 50000:
            cv2.putText(img, "UMARIM BIR GUN", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)
        elif last_value > 10000:
            cv2.putText(img, "BENIDE KABUL EDERSINIZ", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)"""






        """if last_value > 60000:
            cv2.putText(img, "SENI SEVIYORUM", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)"""

        """if last_value > 150000:
            cv2.putText(img, "NAH CEKMEE", (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)"""

        """if xWell*yWell > 6000:
            cv2.putText(img, "PEACE", (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 5, 255),2)"""



    cv2.putText(img, "__________", (160, 130), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)
    cv2.putText(img, "__________", (160, 380), cv2.FONT_HERSHEY_PLAIN, 3, (255, 5, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)

x1listesi.close()
y1listesi.close()
z1listesi.close()