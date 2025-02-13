# class Node:
#     def __init__(self, Data=None, Pointer=None):
#         self.Data = Data
#         self.Pointer = Pointer

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def add(self, Data):
#         newnode = Node(Data)
#         if self.head is None:
#             self.head = newnode
#         else:
#             cur = self.head
#             while cur.Pointer is not None:
#                 cur = cur.Pointer  # Fix: Traverse properly
#             cur.Pointer = newnode  # Fix: Assign new node

#     def print(self):
#         cur = self.head
#         while cur is not None:  # Fix: Traverse all nodes
#             print(cur.Data)  # Fix: Use correct attribute name
#             cur = cur.Pointer

# ll = Linkedlist()

# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.add(4)
# ll.add(5)
# ll.add(6)

# ll.print()




class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer



class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode

        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def add__at__begining(self, data):
        newnode = Node(data)
        newnode.pointer = self.head
        self.head = newnode



    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data) 
            cur = cur.pointer



  



ll = LinkedList()
ll.add(78)
ll.add(56)
ll.add(45)
ll.add(78)
ll.add(56)
ll.add(45)

ll.add__at__begining(96)

ll.print()
                