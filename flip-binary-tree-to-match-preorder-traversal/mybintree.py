class node:
    leftnode = None
    rightnode = None
    value = None
    def __init__( self , inValue):
        self.value = inValue
        #return this


class binTree(object): # returns head of the binary tree we are creating
    head = None
    def __init__( self, nodelist ):
        if isinstance(nodelist, int):
            self.head = node(nodelist)
            return
        nodelist.sort()
        self.head = node(nodelist[len(nodelist)/2])
        self.head.leftnode = self.recinsert( nodelist[0:(len(nodelist)/2)] )
        self.head.rightnode = self.recinsert( nodelist[(len(nodelist)/2)+1:] )
        return
        #for nodeEl in nodelist:
    def recinsert ( self , nodelist):
        # if len(node)
        
        print nodelist
        return node( nodelist[len(nodelist)/2] )
        
