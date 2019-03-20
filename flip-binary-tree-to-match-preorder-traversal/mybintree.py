class node:
    leftnode = None
    rightnode = None
    value = None
    def __init__( self , inValue):
        self.value = inValue
        #return this


class binTree(object): # returns head of the binary tree we are creating
    head = None
    listofTree = []
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
        currentNode = node( nodelist[len(nodelist)/2] )
        if len(nodelist) > 1:
            currentNode.leftnode = self.recinsert( nodelist[0:(len(nodelist)/2)] )
        if len(nodelist) > 2:
            currentNode.rightnode = self.recinsert( nodelist[(len(nodelist)/2)+1:] )
        print nodelist
        return currentNode


    def getList (self):
        self.listofTree = []
        self.orderPrint()
        return self.listofTree[:]

    def orderPrint(self , node = None):
        if node is None:
            node = self.head
        if node.leftnode is not None:
            self.orderPrint( node.leftnode )
        self.listofTree.append(node.value)
        # print node.value
        if node.rightnode is not None:
            self.orderPrint( node.rightnode )
