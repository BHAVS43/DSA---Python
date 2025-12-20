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

#height of binary Tree

def HeightBT(Root):
    if Root == None:
        return -1
    return max(HeightBT(Root.left), HeightBT(Root.right)) + 1
print(HeightBT(Root))