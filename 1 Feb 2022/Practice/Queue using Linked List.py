class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self,value):
        self.front = Node(value)
        self.rear = None
        self.size = 1
    def printqueue(self):
        curr = self.front
        while curr is not None:
            print(curr.value,end = ' ')
            curr = curr.next
    def __sizeof__(self):
        return self.size
    def isEmpty(self):
        return (self.size == 0)
    def getFront(self):
        return self.front.value
    def getRear(self):
        return self.rear.value
    def enque(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front.next = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1
    def deque(self):
            res = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear == None
            self.size -=1
            return res

my_queue = MyQueue(12)
my_queue.enque(10)
my_queue.enque(30)
my_queue.deque()
my_queue.printqueue()
print(my_queue.getRear())
print(my_queue.getFront())
print(my_queue.__sizeof__())
print(my_queue.isEmpty())