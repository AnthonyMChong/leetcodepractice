class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop() # pop without and index will pop the last element

    def push (self , item):
        self.stack.append(item)

    def size (self):
        len(self.stack)

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue (self , item):
        self.queue.append(item)

    def dequeue( self ):
        if len(self.queue > 0):
            return self.queue.pop(0)
        return None