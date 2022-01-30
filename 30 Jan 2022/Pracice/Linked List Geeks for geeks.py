class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.length = 0

    def printlist(self):
        curr = self.head
        while curr is not None:
            print(curr.value,end = ' ')
            curr = curr.next

    def search(self,val):
        curr = self.head
        index = -1
        while curr is not None:
            if curr.value == val:
                return index
            index += 1
            curr = curr.next
        return -1

    def insertBegin(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length +=1

    def insertEnd(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
            self.length +=1

    def insert(self,index,val):
        new_node = Node(val)
        if index<0 or index>self.length:
            raise Exception('Index not valid')
        if index ==1:
            new_node.next = self.head
            self.head = new_node
        curr = self.head
        for x in range(index-1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.length +=1

    def delfirst(self):
        if self.length ==0:
            return None
        elif self.length ==1:
            self.head = None
        else:
            self.head = self.head.next
        self.printlist()
        self.length -= 1

    def delLast(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
        else:
            curr = self.head
            for x in range(self.length -1):
                curr = curr.next
            curr.next = None
        self.length -=1

    def insert_sorted(self,val):
        new_node = Node(val)
        if self.head.value > val:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next.value > val and curr.next is not None:
                    curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.length +=1

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev 
        self.printlist()




linkedlist = LinkedList()
linkedlist.insertEnd(20)
linkedlist.insertEnd(15)
linkedlist.insertEnd(30)
linkedlist.printlist()
linkedlist.insertBegin(40)
linkedlist.printlist()
print(linkedlist.search(20))
linkedlist.insertEnd(33)
linkedlist.printlist()
linkedlist.delfirst()
linkedlist.insert(2,32)
linkedlist.printlist()
linkedlist.delLast()
linkedlist.printlist()
linkedlist.insert_sorted(22)
linkedlist.printlist()
linkedlist.reverse()