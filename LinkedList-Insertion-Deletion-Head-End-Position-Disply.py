class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertionAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def InsertionAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def InsertionAtPosition(self, data, pos):
        new_node = Node(data)
        if pos < 1:
            print("Invalid position")
            return
        
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 1
        while temp != None and count < pos-1:
            temp = temp.next
            count = count + 1
        if temp == None:
            print("Invalid Range")
            return
        new_node.next = temp.next
        temp.next = new_node

    def DeletionAtHead(self):
        if self.head == None:
            print("List is empty")
            return
        self.head = self.head.next

    def DeletionAtEnd(self):
        if self.head == None:
            print("List is empty")
            return
        if self.head.next == None:
            self.head = None
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def DeletionAtPosition(self, pos):
        if pos < 1:
            print("Invalid Position")
            return
        if self.head == None:
            print("List is Empty")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        count = 1
        while temp.next != None and count < pos-1:
            temp.next = temp.next.next
            count = count + 1
        if temp.next == None or temp == None:
            print("Invalid Range")
            return
        temp = temp.next
        
    def display(self):
        if self.head == None:
            print("List is Empty")
        temp = self.head
        while temp != None:
            print(temp.data, end = "->")
            temp = temp.next

L1 = LinkedList()
L1.InsertionAtHead(5)
L1.InsertionAtPosition(10, 2)
L1.InsertionAtPosition(20, 3)
L1.InsertionAtPosition(30, 4)
L1.InsertionAtEnd(40)
L1.display()
#L1.DeletionAtHead()
#L1.DeletionAtEnd()
L1.DeletionAtPosition(3)
print()
L1.display()



