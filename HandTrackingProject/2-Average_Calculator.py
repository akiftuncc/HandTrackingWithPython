# Takes x,y,z values to txt files
# Creates new txt file with average value of x,y,z files

xlistesi = open("x.txt","r")
ylistesi = open("y.txt","r")
zlistesi = open("z.txt","r")

x1listesi = open("txtFiles/x1.txt","w")
y1listesi = open("txtFiles/y1.txt","w")
z1listesi = open("txtFiles/z1.txt","w")

xlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ylist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
zlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

z = True
division = -1
while z:
    division += 1
    for i in range(21):
        try:
            Valx = xlistesi.readline()            
            xlist[i] += float(Valx)
            Valy = ylistesi.readline()
            ylist[i] += float(Valy)
            Valz = zlistesi.readline()
            zlist[i] += float(Valz)
        except:
            z = False
            break
if division == 0:
    print("xlistesi and ylistesi and zlistesi are emtpy")
else:
    for i in range(21):
        xlist[i] /= division
        ylist[i] /= division
        zlist[i] /= division
        x1listesi.write(str(xlist[i])+"\n")
        y1listesi.write(str(ylist[i]) + "\n")
        z1listesi.write(str(zlist[i]) + "\n")

xlistesi.close()
ylistesi.close()
zlistesi.close()

x1listesi.close()
y1listesi.close()
z1listesi.close()




