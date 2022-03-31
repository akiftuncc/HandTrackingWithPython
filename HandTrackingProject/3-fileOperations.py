import os

old_nameX = r"txtfiles/x1.txt"
old_nameY = r"txtfiles/y1.txt"
old_nameZ = r"txtfiles/z1.txt"

x = input("x file name: ")
y = input("y file name: ")
z = input("z file name: ")

new_nameX = r"txtfiles/{}.txt".format(x)
new_nameY = r"txtfiles/{}.txt".format(y)
new_nameZ = r"txtfiles/{}.txt".format(z)

os.rename(old_nameX, new_nameX)
os.rename(old_nameY, new_nameY)
os.rename(old_nameZ, new_nameZ)

Xtxt_names = open("txtFiles/0_Xnames.txt", "a")
Ytxt_names = open("txtFiles/0_Ynames.txt", "a")
Ztxt_names = open("txtFiles/0_Znames.txt", "a")

Xtxt_names.write(f"\n{x}")
Ytxt_names.write(f"\n{y}")
Ztxt_names.write(f"\n{z}")








