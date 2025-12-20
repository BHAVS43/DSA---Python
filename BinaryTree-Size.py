class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(Root):
    if Root == None:
        return
    print(Root.data, end=" ")
    PreOrder(Root.left)
    PreOrder(Root.right)

Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(50)
Root.right.left = Node(60)
Root.right.right = Node(70)

PreOrder(Root)
print()

#size of binary Tree

def SizeBT(Root):
    if Root == None:
        return 0
    return 1+SizeBT(Root.left)+SizeBT(Root.right)
print(SizeBT(Root))