# class binTree:
#     def __init__(self , treeVals ):
#         for 

class Node:
    def __init__(self , data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert (self , data):
        if self.data != None:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:   # if this is the first data inserted, make the data the root node
            self.data
        
    def preOrderTraversal( self , curNode ):
        res = []
        if curNode != None:
            res.append(curNode.data)
            res = res + self.preOrderTraversal(curNode.left)
            res = res + self.preOrderTraversal(curNode.right)
        return res

    def PostorderTraversal( self, curNode ):
        res = []
        if curNode:
            res = self.PostorderTraversal( curNode.left )
            res = res + self.PostorderTraversal( curNode.right )
            res.append(curNode.data)
        return res

    def printme(self):
        print self.data

    def bfstravesal ( self , start ):
        visited = []
        queue = [start ]
        while (len(queue) > 0):
            curNode = queue.pop( 0 )
            if curNode not in visited:
                visited.append(curNode)
                print curNode.data

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                
                # neighbors = graph[node]
                # for n in neighbors:
                #     queue.append(n)
    
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodeQueue = []
        nodeQueue.append(root)
        freezeQueue = False
        
        while len(nodeQueue) > 0 :
            curNode = nodeQueue.pop(0)
            if curNode.left is not None:
                if freezeQueue:
                    return False
                nodeQueue.append(curNode.left)
            else:
                freezeQueue = True
                
            if curNode.right is not None:
                if freezeQueue:
                    return False
                nodeQueue.append(curNode.right)
                
            if ((curNode.left is None) or (curNode.right is None)):
                freezeQueue = True
                
        return True

        def dfs (self , curNode):
            print curNode.data

            if curNode.left:
                self.dfs(curNode.left)
            if curNode.right:
                self.dfs(curNode.right)

    def serialize (self , root):
        serialList = []
        bfsQueue = []

        bfsQueue.append(root)
        serialList.append(root.data)

        lastRealNode = 0

        while (len(bfsQueue) > 0):
            curNode = bfsQueue.pop(0)
            if curNode.left:
                serialList.append(curNode.left.data)
                bfsQueue.append(curNode.left)
                lastRealNode = curNode.left
            else:
                serialList.append("N")

            if curNode.right:
                serialList.append(curNode.right.data)
                bfsQueue.append(curNode.right)
                lastRealNode = curNode.right
            else:
                serialList.append("N")

            if curNode == lastRealNode:
                # serialList = str(serialList)
                # return ','.join(serialList)
                serialList = [str(x) for x in serialList]
                return ','.join(serialList)

        return None

    def deserialize (self , serialstr):

        serialList = serialstr.split(',')

        dserialQueue = []
        curNode = Node(serialList.pop(0))
        dserialQueue.append(curNode)

        while ( len(serialList) > 0):
            curNode = dserialQueue.pop(0)

            if curNode == 'N':
                serialList.pop



    #     root = Node( int(serialList[0]) )

    #     for s in serialList[1:-1]:
    #         if s != 'N':
    #             curNode = Node(int(s))

    # def ninsert (self , root , data ):

    #     if root == None:
    #         root = Node(data)
    #     elif root.left == None:
    #         root.left = Node(data)
    #     elif root.right == None:
    #         root.right = Node(data)




if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print root.serialize(root)
    # print(root.preOrderTraversal(root))
    # print(root.PostorderTraversal(root))
    # # root.bfstravesal(root)
    # root.dfs(root)