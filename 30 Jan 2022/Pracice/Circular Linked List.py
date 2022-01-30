class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

class CircularLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        new_node.next = self.head
        self.length = 1

    def printCircular(self):
        print(self.head.value,end =' ')
        curr = self.head.next
        while curr != self.head:
            print(curr.value,end = ' ')
            curr = curr.next

    def insertBegin(self,value):
        new_node = Node(value)
        curr = self.head
        while curr.next != self.head and curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head =new_node
        self.length +=1
        self.printCircular()

    # def insertBegin(self,value):
    #     new_node = Node(value)
    #     new_node.next = self.head.next
    #     self.head.next = new_node
    #     self.head.value, new_node.value = new_node.value,self.head.value
    #     self.printCircular()
    #     self.length +=1

    def insertEnd(self,value):
        new_node = Node(value)
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.printCircular()
        self.length +=1

    # def insertEnd(self,value):
    #     new_node = Node(value)
    #     new_node.next = self.head.next
    #     self.head.next = new_node
    #     new_node.value,self.head.value = self.head.value,new_node.value
    #     self.head = new_node
    #     self.printCircular()
    #     self.length +=1

    def delHead(self):
        if self.length == 1:
            return None
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head.next = None
            self.head = curr.next
        self.printCircular()
        self.length-=1

    # def delHead(self):
    #     if self.length ==1:
    #         return None
    #     else:
    #         self.head.value = self.head.next.value
    #         self.head.next = self.head.next.next
    #     self.printCircular()
    #     self.length-=1






circular_linkelist = CircularLinkedList(10)
circular_linkelist.printCircular()
circular_linkelist.insertBegin(20)
circular_linkelist.insertEnd(12)
circular_linkelist.delHead()
