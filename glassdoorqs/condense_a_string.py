
def condenseString ( spacedString ): 
    """
    Remove all spaces from a string and return it

    @param - spacedString : the string to be condensed 

    return - the condensed string

    """

    #initializing a list with string in list format
    returnList = []

    #iterate through each element in original string an check for character to be removed
    for x in list(spacedString):
        if x != ' ':
            #adding valid character into list
            returnList.append(x)

    return ''.join(returnList)
