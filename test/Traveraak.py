
class Node:
     Pointer = None
    
     def __init__(self,data):
          self.data = data


lap1 = Node("node1")

lap2 = Node("node2")

lap3 = Node("node3")
lap4 = Node("node4")

lap5 = Node("node5")

lap6 = Node("node6")
lap7 = Node("node7")

lap1.Pointer = lap2
lap2.Pointer = lap3
lap3.Pointer = lap4
lap4.Pointer = lap5
lap5.Pointer = lap6
lap6.Pointer = lap7









# print(lap1)
# print(lap1.data)
# print(lap1.Pointer)
# print("----------------------------------")
# print(lap2)
# print(lap2.data)
# print(lap2.Pointer)
# print("----------------------------------")
# print(lap3)
# print(lap3.data)
# print(lap3.Pointer)
# print("----------------------------------")


current = lap1

while (current is not None):
     print(current.data)
     print(current)
     current = current.Pointer
    

