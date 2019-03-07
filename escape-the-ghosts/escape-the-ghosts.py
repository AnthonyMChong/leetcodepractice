
#you are at 0,0
#dest is at target[0] target[1]
#true for 100% can escape False for cannot escape
#will need to change if ghost can be both farther away from the target than you AND catch you...
#possibly need to check every tile of your movement to see if a ghost could have reached within time
def canEscape (ghosts , target):    #ith ghost is at ghost[i][0],ghost[i][1]
    turn = 0
    ghostfinish = None
    for ghost in ghosts:
        thisfinish = abs(ghost[0] - target [0]) + abs(ghost [1] - target[1])
        if ghostfinish == None:
            ghostfinish = thisfinish
        elif thisfinish < ghostfinish:
            ghostfinish = thisfinish
        if (abs(target [0]) + abs(target[1])) > thisfinish:
            return False
    return True # if we reach at the same time


myghosts = [[-5,0],[-1,0],[10,10]]
mytarget = [4,4]
print canEscape (myghosts , mytarget)
