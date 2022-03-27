def listappender(xyztext,xyzlist):
    for i in xyztext:
        xyzlist.append(float(i[:-1]))

def listminus(lists,xeqlists):     #(xortlist,xeq1_list)
    counti = -1
    for i in range(len(lists)):
        counti += 1
        countj = -1
        for j in range(21):
            countj += 1
            val = abs(lists[i]-lists[countj])
            xeqlists[counti].append(val)
        if counti == 20:
            counti = -1


def translator(currentlist,avglist):   #zeqlist   zeq1list
    countValues = 0
    counti = 0
    for i in range(len(avglist)):
        counti+=1
        countj = 0
        for j in range(21):
            countj +=1
            if avglist[i][j]*8/10 < currentlist[i][j] and avglist[i][j]*12/10 > currentlist[i][j]:
                countValues += 1
    return countValues


lists = ["42 eleman"]
xeqlists = ["0 eleman"]
