class Node:
    def __init__(self, Data=None, Pointer=None):
        self.Data = Data
        self.Pointer = Pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.Pointer is not None:
                cur = cur.Pointer
            cur.Pointer = new_node

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.Data, end=" -> ")
            cur = cur.Pointer
        print("None")


ll = LinkedList()
ll.add(6)
ll.add(78)
ll.print_list()
