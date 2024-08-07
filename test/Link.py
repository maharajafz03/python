
class Node:
    memory = None
    address = None

    def __init__(self,memory,address):
        self.memory = memory
        self.address = address



# -----------Node--------------

Head = Node("node1")

node2 = Node("node2")

node3 = Node("node2")


# ----------------Linkedlist-----------------

Head.address = node2
node2.address = node3
node3.address = Head



print(Head.memory)
print(Head.address)
print(node2.memory)
print(node2.address)
print(node3.memory)
print(node3.address)
