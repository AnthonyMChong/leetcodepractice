class LinkedNode():
    def __init__(self , data):
        self.next = None
        self.data = data


class LinkedList():
    def __init__(self):
        self.head = None

    def InsertAtHead(self , newHeadData):

        newNode = LinkedNode(newHeadData)

        if self.head :
            newNode.next = self.head

        self.head = newNode

    def remove(self , removeData):
        curNode = self.head

        if curNode.data == removeData:
            self.head = self.head.next
        
        while curNode.next:
            if curNode.next.data == removeData:
                curNode.next = curNode.next.next
                break
            curNode = curNode.next


    def InsertAtTail(self, newTailData):

        newNode = LinkedNode (newTailData)
        if self.head:
            curNode = self.head
            while curNode.next:
                curNode = curNode.next

            curNode.next = newNode

        else:
            self.head = newNode

    def printList (self):

        curNode = self.head

        while curNode:
            print curNode.data
            curNode = curNode.next

    def printListreverse (self):

        printStack = []

        curNode = self.head

        while curNode:
            # printStack.push(curNode.data) unfortunately lists do not have push... insert(index, data)
            printStack.insert( 0 , curNode.data )
            curNode = curNode.next

        print printStack 

    def InsertInOrder(self , newData):
        newNode = LinkedNode (newData)

        if self.head:
            curNode = self.head
            while curNode.next:
                if curNode.next.data > newNode.data:
                    newNode.next = curNode.next
                    curNode.next = newNode
                    break
                curNode = curNode.next
            curNode.next = newNode
        else:
            self.head = newNode

if __name__ == "__main__":
    # initialize our head node
    intolist = [2,4,8,6,10]
    head = LinkedNode( 1 )
    linkedList = LinkedList()
    linkedList.head = head
    # initialize linked list finsihed

    for i in intolist:
        linkedList.InsertInOrder (i)

    linkedList.remove(1)

    linkedList.remove(10)

    linkedList.remove(8)

    linkedList.remove(6)

    linkedList.printList()
    linkedList.printListreverse()