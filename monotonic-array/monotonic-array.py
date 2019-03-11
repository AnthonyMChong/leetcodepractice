def ismonotonic ( inlist ): # will use mode flag to check 0 monotone -1 if dec , 1 if inc
    monoflag = 0
    preVal = None
    for checklist in inlist:
        if preVal == None:
            preVal = checklist
        elif (checklist > preVal) :
            if (monoflag < 0):
                return False
            monoflag = 1
        elif (checklist < preVal) :
            if (monoflag > 0):
                return False
            monoflag = -1
        preVal = checklist

    return True

mylist = [ 1, 1, 2, 2, 5, 6, 6, 7, 11 , 1]
mylist = mylist[::-1]
print mylist
print ismonotonic(mylist)