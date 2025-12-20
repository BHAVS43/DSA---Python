class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
Root = Node(78)
def BSTInsertion(Root, data):
    if Root == None:
        return Node(data)
    if Root.data < data:
        Root.right = BSTInsertion(Root.right, data) 
    else:
        Root.left = BSTInsertion(Root.left, data) 
    return Root

def InOrder(Root):
    if Root == None:
        return
    InOrder(Root.left)
    print(Root.data, end = " ")
    InOrder(Root.right)

BSTInsertion(Root, 77)
BSTInsertion(Root, 94)
BSTInsertion(Root, 41)
BSTInsertion(Root, 12)
BSTInsertion(Root, 5)
BSTInsertion(Root, 15)
BSTInsertion(Root, 102)
BSTInsertion(Root, 91)
BSTInsertion(Root, 90)
BSTInsertion(Root, 92)

InOrder(Root)
print()

def mini(Root):
    temp = Root
    while temp.left:
        temp = temp.left
    return temp

def BSTDeletion(Root, data):
    if Root == None:
        return Root
    
    if data < Root.data:
        Root.left = BSTDeletion(Root.left, data)
    elif data > Root.data:
        Root.right = BSTDeletion(Root.right, data)
    else:
        if Root.left == None:
            return Root.right
        elif Root.right == None:
            return Root.left

        suc = mini(Root.right)
        Root.data = suc.data
        Root.right = BSTDeletion(Root.right, suc.data)

    return Root

Root = BSTDeletion(Root, 91)
InOrder(Root)
    