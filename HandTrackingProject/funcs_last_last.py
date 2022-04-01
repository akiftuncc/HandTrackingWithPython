# Some funcs
def listappender(xyztext,xyzlist):
    for j in xyztext:
        xyzlist[len(xyzlist)-1].append(float(j[:-1]))

def listminus(lists,xeqlists):     #(xortlist,xeq1_list)
    # xort list oluşur 2 boyutlu olarak şuanda 2*21
    # xeq1_list oluşur 3 boyutlu olarak şuanda 2*21*21
    for i in range(len(lists)):
        for j in range(21):
            for k in range(21):
                val = lists[i][j]-lists[i][k]
                xeqlists[i][j].append(abs(val))

def listminus_current(xcurrent,xeqlists):
    for i in range(21):
        for j in range(21):
            val = xcurrent[i]-xcurrent[j]
            xeqlists[i].append(abs(val))


def translator(currentlist,avglist):   #zeqlist   zeq1list
    liste = []
    for i in range(len(avglist)):
        count = 0
        for j in range(21):
            for k in range(21):
                a = currentlist[j][k]
                b = avglist[i][j][k]
                if a*120/100 > b and a*82/100 < b:
                    count+=1
        liste.append(count)
    return liste







lists = ["42 eleman"]
xeqlists = ["0 eleman"]
