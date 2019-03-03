import pdb
def findCombinations( k , n , startingnumber = 0):   # all combinations of 3 numbers that will add up to n
    solList = []
    if ( (startingnumber > n)):
        return None #soultion is not viable
    if (k == 1):
        return n    # when we only have 1 space it is equal to the number
    for testitem in range(startingnumber , n):
        possibleSol = testitem + 1    # starting higher to prevent duplicates in each entry
        leftover = n - possibleSol  # the leftover sum
        returnlist = findCombinations( k-1 , leftover , possibleSol)
        if returnlist is not None:
            solList.append(possibleSol)
    return solList

def twoSum (n , start): #test function where the sum  n consists of start and another int that is larger
    if (start > n):
        return None
    else :
        return n - start

def twoSumRec (k , n , start = 0): #test function where the sum  n consists of start and another int that is larger
    retList = []
    if (start > n or k < 1):
        return None
    if (k == 1):
        return n    # when we only have 1 space it is equal to the number
    else :
        retList.append(start)
        recReturn = twoSumRec(k -1 , n - start , start)
        if recReturn is not None:
            retList.append(recReturn)
        else:
            return None

def twoSumRecHelper (k , n ):
    retList = []
    
    for myInput in range (1,n):
        twoSumRecRet = twoSumRec(k , n , myInput)
        if twoSumRecRet is not None:
            retList.append(twoSumRecRet)
    return retList



answer = twoSumRecHelper( 2 , 3 )
print "our soulution:"
print answer