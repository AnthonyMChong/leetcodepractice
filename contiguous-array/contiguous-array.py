def maxSubList( inList ): # return a max length of equal number of 0 and 1
    maxlens = []
    reflist = [None for i in range(len(inList))]
    reflist[0] = [-1]
    maxLen = 0
    curlen = 0
    for bindex in range (0 , len(inList)):
        # check the new value
        if inList[bindex] == 1:
            curlen += 1
        else:
            curlen -= 1
        maxlens.append(curlen)
        if reflist[curlen] == None:
            reflist[curlen] = []
        reflist[curlen].append(bindex)
    maxLen = 0
    for lengths in reflist:
        if lengths is not None:
            maxatEqual = max(lengths) - min (lengths)
            if maxatEqual > maxLen:
                maxLen = maxatEqual
    return maxLen


    #     # either save the list or restart the count from previous
    #     if max1 == max0 and maxLen < curLen:
    #         listHead = bindex
    #         listTail = bindex - ( max1 + max0 )
    #     #retList.append(inList[bindex])
    # return retList 


testList = [0, 0 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 1 , 1]
print maxSubList(testList)