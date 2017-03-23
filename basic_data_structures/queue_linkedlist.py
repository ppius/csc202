from node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.back = None
        self.N = 0

    def enqueue(self, data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.back = self.front
        else:
            self.back.setNext(temp)
            self.back = self.back.getNext()
        self.N += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front
        if self.front.getNext() is None:
            self.front = None
            self.back = None
        else:
            self.front = self.front.getNext()
        self.N -= 1
        return temp


    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N
