def listappender(xyztext,xyzlist):
    for i in xyztext:
        xyzlist.append(float(i[:-1]))

def listminus(lists,xeqlists):     #(xortlist,xeq1_list)
    liste = [0,4,8,12,16,20,1,5,9,13,17]
    count = -1
    for i in liste:
        count += 1
        for j in range(21):
            val = abs(lists[i]-lists[j])
            xeqlists[count].append(val)

def translator(avglist,currentlist):   #zeqlist   zeq1list
    count = 0
    for i in range(11):
        for j in range(21):
            if avglist[i][j]*8/10 < currentlist[i][j] and avglist[i][j]*12/10 > currentlist[i][j]:
                count += 1


    return count


