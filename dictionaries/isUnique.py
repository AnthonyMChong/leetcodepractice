def isunique ( uniquestr ):
    chardict = {}
    for unichar in uniquestr:
        if chardict.get(unichar) == None:   # checking if char is unique or first of its kind
            chardict[unichar] = [ unichar ]
        else:
            print chardict
            return False

    print chardict

def isuniquenomem ( uniquestr ):
    pass
    
if __name__ == "__main__":
    testString = "abcdefgoih"
    print isunique (testString)
    testString = "abcdefgfih"
    print isunique (testString)
