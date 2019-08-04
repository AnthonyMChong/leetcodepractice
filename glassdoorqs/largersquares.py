'''
given 3 numbers find the sum of squares of the larger 2 numbers


'''

def findLargerSquares( a , b , c ):
    returnSum = 0

    a_or_b = 0

    # compare the first two variables for the largest
    if a > b:
        # in the case a is larger than b, set a_or_b to b to compare later
        returnSum += a**2
        a_or_b = b
    else:
        # in the case b is larger than a, set a_or_b to a to compare later
        returnSum += b**2
        a_or_b = a

    if a_or_b > c:
        returnSum += a_or_b**2
    else:
        returnSum += c**2

    return returnSum
