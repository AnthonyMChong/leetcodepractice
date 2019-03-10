def robHouses( houses ):
    route1 = 0
    route2 = 0
    for houseIndex in range (0 , len(houses)):
        if ( houseIndex % 2 == 0 ): # check which route we are using
            route1 += houses[houseIndex]
        else:
            route2 += houses[houseIndex]
    if route1 > route2:
        return route1
    elif route1 == route2:  # if we get the same amount of money, might as well rob less
        if ( len(houses) % 2 == 0 ):
            return route2
        else:
            return route1
    else:
        return route2

myhouses = [2,7,9,3,1,2]
print robHouses(myhouses)