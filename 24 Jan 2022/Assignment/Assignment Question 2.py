# Defining the Node class which initialises a Node.
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining the LinkedList class to create and empty linkedlist.
class LinkedList:
    # Function to initialize the LinkedList object
    def __init__(self):
        self.head = None
        self.last_node = None
    
    # Function to add elements to the LinkedList
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    # Function to print the LinkedList
    def printLinkedlist(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

# Initialising the Linkedlist
a_llist = LinkedList()
# Input for numbers of elements to be added to the LinkedList
n = int(input('How many elements would you like to add? '))
# Iterating for n numbers of times to take the inputs for numbers to be added in the LinkedList.
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end='')
a_llist.printLinkedlist()
