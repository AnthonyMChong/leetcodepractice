class Solution(object):
    def majorityElement( self , inlist ):
        #print inlist
        inlist.sort()
        print inlist
        nelements = len( inlist ) / 2
        for checkmaj in  range ( 0 , len(inlist) - 1):
            if checkmaj + nelements >= len(inlist):
                print "no majority elements"
                return None
            elif inlist[checkmaj + nelements] == inlist[checkmaj]:
                return inlist[checkmaj]

if __name__ == "__main__":
    mylist = [2,2,1,1,1,2,2, 2, 1 ,1,3,1 ,1 ]
    mySolution = Solution()
    print mySolution.majorityElement( mylist )