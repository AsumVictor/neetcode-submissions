class Node:
    
    def __init__(self, val):
        self.val = val;
        self.next = None

class MinStack:

    """
    List: pop from it (1) shift: (n)
    top: constant
    Linkedlist: 
    variable to track minimum.
    if the val i'm pusing is less than the min then change

    1: [4, 2]
    2: [5, 0]
    3: [0, ]

    curr: 0
    curr: 3
    """

    def __init__(self):
        self.head = None
        
    def push(self, val: int) -> None:

        if not self.head:
            self.head = Node((val, val))
        else:
            newNode = Node((val, min(self.head.val[1], val)))
            newNode.next = self.head
            self.head = newNode

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        if self.head:
            return self.head.val[0]

    def getMin(self) -> int:
        return self.head.val[1]
        
