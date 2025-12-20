class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def InOrder(Root):
    if Root == None:
        return
    InOrder(Root.left)
    print(Root.data, end = " ")
    InOrder(Root.right)
    
Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(50)
Root.right.left = Node(60)
Root.right.right = Node(70)
InOrder(Root)
    
    
