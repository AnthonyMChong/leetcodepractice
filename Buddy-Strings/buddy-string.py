class Solution:
    def findBuddyString( self , str1 , str2 ): # a function to determine if the strings are equal after swapping a pair of chars 
        str1 = list(str1)
        str2 = list(str2)
        str1len = len (str1)
        str2len = len (str2)
        if str1len is not str2len:
            return False
        diffcount = 0
        diffarray = []
        sameletter = 0
        sameletter = []
        for compare in range ( 0 , str1len - 1):
            if not (str1[compare] == str2[compare]):
                diffcount += 1
                diffarray.append(compare)
                print str1[compare] , "  " , str2[compare]
            if diffcount == 2:
                #pdb.set_trace()
                charbuff = (str1[diffarray[0]])
                str1[diffarray[0]] = str1[diffarray[1]]
                str1[diffarray[1]] = charbuff
                # charbuff = (str2[diffarray[0]])
                # str2[diffarray[0]] = str2[diffarray[1]]
                # str2[diffarray[1]] = charbuff
                if str1 == str2:
                    return True
        return False
        
        return False 
teststr1 = "allison"
teststr2 = "ollisan"
Solution = Solution()

print Solution.findBuddyString(teststr1 , teststr2)