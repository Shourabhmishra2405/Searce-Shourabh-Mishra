class Myhash:
    def __init__(self,capacity):
        self.cap = capacity
        self.table = [-1]*capacity
        self.size = 0
    def hash(self,x):
        return x% self.cap
    def search(self,value):
        h = self.hash(value)
        t = self.table
        i = h
        while t[i]!= -1:
            if t[i] ==value:
                return True
            i = (i+1)%self.cap
            if i==h:
                return False
        return False
    def insert(self,value):
        if self.size == self.cap:
            return False
        if self.search(value) == True:
            return False
        i = self.hash(value)
        while t[i] not in (-1,-1):
            i = (i+1)%self.cap
        t[i] = value
        self.size +=1
        return True
    def remove(self,value):
        i = self.hash(value)
        t = self.table
        while t[i] != -1:
            if t[i] == value:
                t[i]= -2
                return True
            i = (i+1) % self.cap
            if i==h:
                return False
        return False

# use None for empty and reference to dummy node in the deleted slot


