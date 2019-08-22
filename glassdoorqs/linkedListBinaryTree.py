from tree import *
from linkedlist import *

def tree2LinkedList(root):
    depthList = []

def BFStree2linkedlist ( node ):
    queue = []
    queue.append (node)
    queue.append (None)
    depthcount = 0
    depthList = [LinkedList()]

    while (len(queue)):
        curnode = queue.pop(0)

        if curnode == None: # if we are reaching a new depth add another None to signify another depth
            if len(queue) == 0: # no more elements 
                break
            else:
                queue.append(None)
                depthcount += 1
                depthList.append(LinkedList())
            continue

        if curnode.left is not None:
            queue.append(curnode.left)
        if curnode.right is not None:
            queue.append(curnode.right)

        print curnode.data
        print "depth : ", depthcount
        depthList[depthcount].InsertAtTail(curnode.data)

    return depthList

def DFSfindAncestor ( root , children , ancestorList):

    if children[ 0 ] == root.data:
        return root

    for node in (root.left , root.right):
        if node:
            search = DFSfindAncestor (node , children , ancestorList)
            if search is not None:
                ancestorList.append(root)
                return search
    # if root.left:
    #     leftsearch =  DFSfindAncestor (root.left , children , ancestorList)
    #     if leftsearch is not None:
    #         ancestorList.append(root)
    #         return leftsearch

    # if root.right:
    #     rightsearch = DFSfindAncestor (root.right , children , ancestorList)
    #     if rightsearch is not None:
    #         ancestorList.append(root)
    #         return rightsearch


if __name__ == "__main__":

    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    # bfsll = BFStree2linkedlist(root)

    # for idx , LL in enumerate(bfsll):
    #     print "Depth %i :" %(idx)
    #     LL.printList()

    child1ancestors = []
    dfsan = DFSfindAncestor ( root , [14,42] , child1ancestors )
    print dfsan
    print child1ancestors

    child2ancestors = []
    dfsan = DFSfindAncestor ( root , [42,14] , child2ancestors )
    print dfsan
    print child2ancestors