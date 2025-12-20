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

    def GoodBad(self):
        freq = {}
        temp = self.head
        flag1 = True

        while temp:
            if temp.data in freq:
                freq[temp.data] = freq[temp.data] + 1
            else:
                freq[temp.data] = 1
            temp = temp.next

        for value in freq:
            if freq[value] > 1:
                flag = False
                print("Bad List")
                return
            else:
                print("Good List")
                return


    def Duplicate(self):
        unique = set()
        temp = self.head
        flag = True
        while temp:
            if temp.data  in unique:
                flag = False
                print("Bad List")
                return
            else:
                unique.add(temp.data)
                temp = temp.next
        if flag:
            print("Good List")
            
                
        

            
L1 = LinkedList()
L1.InsertionAtHead(20)
L1.InsertionAtHead(40)
L1.InsertionAtPosition(10, 2)

L1.InsertionAtEnd(30)
L1.display()
print()
L1.GoodBad()
L1.Duplicate()



