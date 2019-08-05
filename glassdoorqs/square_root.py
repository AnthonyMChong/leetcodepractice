'''
find square root of a number without using external functions

approach: we know squares of numbers will be significantly increasing with a increasing input. as in we will see a positive trend.
knowing this we can view the results of squareroots to be "sorted"

will try a binary search type on the squares of return values we are "guessing"

'''

def squareroot ( squaredNumber ):
    """
    function: squareroot - find the square root of given number

    @param: squaredNumber - the number to be square-rooted

    return - squareroot fo squaredNumber
    """
    if ( squaredNumber < 0):
        #return/print expected error value if we get an impossible to reach number such as a negative
        return -1
    
    return squarebinsearch (squaredNumber , 0 , squaredNumber)
    


def squarebinsearch ( findx , low , high):

    currentx = (low + high) /2

    currentxsqrd = currentx**2

    if (currentxsqrd > findx):
        return squarebinsearch ( findx , low , currentx )
        
    if (currentxsqrd < findx):
        return squarebinsearch ( findx , currentx , high )

    if (currentxsqrd == findx):
        return currentx

    return currentx

if __name__ == '__main__':
    print squareroot(25)