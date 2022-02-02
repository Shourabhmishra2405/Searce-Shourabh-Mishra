class MyQueue:
    def __init__(self,capacity):
        self.l = [None]*capacity
        self.cap = capacity
        self.size = 0
        self.front = 0
        self.rear = (self.front + self.size -1)%self.cap
    def printqueue(self):
        print(self.l[self.front:self.rear])
    def getFront(self):
        if self.size == 0:
            return None
        else:
            return self.l[self.front]
    def getRear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size -1)% self.cap
            return self.l[rear]
    def enque(self,value):
        if self.size == self.cap:
            return None
        else:
            rear = (self.front + self.size - 1)% self.cap
            rear = (rear+1)%self.cap
            self.l[rear] = value
            self.size = self.size +1
    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front +1)%self.cap
            self.size = self.size -1
            return res

my_queue = MyQueue(5)
my_queue.enque(15)
my_queue.enque(12)
print(my_queue.deque())
my_queue.printqueue()