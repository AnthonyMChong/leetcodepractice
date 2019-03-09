def canPlaceFLowers(flowerbed , numflower):
    for plotindex in range(0,len(flowerbed)-1):
        if (flowerbed[plotindex - 1] == 0 or plotindex == 0) and ( flowerbed[plotindex + 1] == 0 or plotindex == len(flowerbed)) and (flowerbed[plotindex] == 0):
            numflower -= 1
            flowerbed[plotindex] = 1
        if numflower < 1:
            print flowerbed
            return True
    print flowerbed
    return False


myflowerbed = [0, 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1]
mynumflowers = 3
print canPlaceFLowers(myflowerbed , mynumflowers)