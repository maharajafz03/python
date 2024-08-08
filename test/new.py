
class Node:
    pointer = None

    def __init__(self, data):
        self.data = data

class chain:

    def __init__(self):
        self.head = None
        

    def add(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while(cur.pointer is not None):
                cur = cur.pointer
            cur.pointer = newNode

    
    def print(self):
        cur = self.head

        while(cur is not None):
            print(cur)
            print(cur.data)
            print(cur.pointer)
            cur = cur.pointer


chains = chain()

chains.add("node1")
chains.add('node2')
chains.add("node3")
chains.print()