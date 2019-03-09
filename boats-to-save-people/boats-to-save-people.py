def findboatNum( people , limit):
    boats = 0
    people.sort()
    if people[-1] > limit:
        return -1
    while len(people) > 0:   #allocate boats until there are no more people
        heaviestpersonindex = len(people) - 1
        # if heaviestpersonindex > 0:     # if there are peopel to pair
        #     if people[-1] + people[0] <= limit: #check if we can pair the heaviest person with smallest
        #         people.pop(heaviestpersonindex)
        #         people.pop(0)
        #         boats += 1
        #         continue
        if (people[-1] + people[0] <= limit) and (heaviestpersonindex > 0): #check if we can pair the heaviest person with smallest
            people.pop(heaviestpersonindex)
            people.pop(0)
            boats += 1
            continue
        else:
            # print "trying to pop: ", heaviestpersonindex , " from: ", people
            people.pop(heaviestpersonindex)
            boats += 1
    return boats



mypeople = [ 3 , 4 , 4, 5, 2, 3, 1, 2, 3 , 1 , 1]
mylimit = 5
print findboatNum(mypeople , mylimit)