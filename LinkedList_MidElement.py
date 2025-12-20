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

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end = "->")
            temp = temp.next

    def MidEle(self):
        if self.head = None:
            print("List is Empty")
            return
            
        Slow = self.head
        Fast = self.head
 
        while Fast != None and Fast.next != None and Fast.next.next != None:
            Slow = Slow.next
            Fast = Fast.next.next
        print(Slow.data)
                  
            
L1 = LinkedList()
L1.InsertionAtHead(20)
L1.InsertionAtHead(40)
L1.InsertionAtPosition(10, 2)

L1.InsertionAtEnd(30)
L1.display()
print()
L1.MidEle()



