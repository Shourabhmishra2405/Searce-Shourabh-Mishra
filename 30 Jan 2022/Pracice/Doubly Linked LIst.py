class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.prev = None
        self.next = None
        self.length = 1

    def insertBegin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        self.printlist()

    def printlist(self):
        curr = self.head
        while curr:
            print(curr.value, end=' ')
            curr = curr.next

    def insertEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        self.length += 1
        self.printlist()

    def delHead(self):
        if self.length == 1:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.printlist()

    def delLastNode(self):
        if self.length == 1:
            return None
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        self.length -= 1
        self.printlist()

    def reverselist(self):
        if self.head.next ==None:
            self.head.next = self.head.prev
            self.head.prev = self.head.next
        else:
            curr = self.head
            while curr is not None:
                head = curr
                curr.prev,curr.next = curr.next,curr.prev
                curr = curr.prev
            self.head = head
        self.printlist()

doubly_linkedlist = DoublyLinkedList(10)
doubly_linkedlist.insertBegin(20)
doubly_linkedlist.insertBegin(12)
doubly_linkedlist.delHead()
doubly_linkedlist.delLastNode()
doubly_linkedlist.insertEnd(33)
doubly_linkedlist.reverselist()
