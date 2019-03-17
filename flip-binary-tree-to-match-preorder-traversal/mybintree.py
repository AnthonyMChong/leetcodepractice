class node:
    leftnode = None
    rightnode = None
    value = None
    def __init__( self , inValue):
        self.value = inValue
        #return this


class binTree: # returns head of the binary tree we are creating
    head = None
    def __init__( self, nodelist ):
        isinstance(nodelist, int):
            self.head = node(nodelist)
            return
        nodelist.sort()
        head = node(nodelist[len(nodelist)/2])
        #for nodeEl in nodelist:
        
