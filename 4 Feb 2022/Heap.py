import math


class MyMinHeap:
    def __init__(self):
        self.arr = []
    def parent(self,i):
        return (i-1)/2
    def lchild(self,i):
        return (2*i+1)
    def rchild(self,i):
        return (2*i +2)
    def insert(self,value):
        self.arr.append(value)
        i = len(self.arr)-1
        while i>0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i],self.arr[p] = self.arr[p],self.arr[i]
            i =p

    def MinHeapify(self,i):
        arr = self.arr
        lt = self.lchild(i)
        rt = self.rchild(i)
        smallest = i
        n = len(arr)
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt<n and arr[rt] < arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[smallest],arr[i] =arr[i],arr[smallest]
            self.MinHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        n = len(arr)
        if n==0:
            return math.inf
        res = arr[0]
        arr[0] = arr[n-1]
        arr.pop()
        self.MinHeapify(0)
        return res

    def decreasekey(self,i,value):
        arr = self.arr
        arr[i] = value
        while i >0 and arr[i] < arr[self.parent(i)]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p

    def deletekey(self,i):
        n = len(self.arr)
        if i >n:
            return
        else:
            self.decreasekey(i,-math.inf)
            self.extractMin()

class MyMinHeap2:
    def __init__(self, l =[]):
        self.arr = l
        i = (len(l)-2)//2
        while i >= 0:
            self.minHeapify(i)
            i = i-1


