

class Node:
  Pointer = None 
  
  def __init__(self,data):
    self.data = data


class Link:
  
  def __init__(self):
    self.head = None


  def add(self,data):
    newnode = Node(data)
    if self.head is None:
      self.head = newnode

    else:
      cur = self.head
      while (cur is not None):
        cur.Pointer = newnode

  def print(self,data):
    print(self.data)
    

  def remove(self,data):
    if(self.head.Pointer is not None):
         if(self.head.data == data):
            self.head = self.head.Pointer 
         else:
           cur = self.head
           while(cur.Pointer is not None and cur.Pointer.data != data):
             cur = cur.Pointer

             if cur.pointer is not None:
               cur.pointer =  cur.pointer.pointer
    
    else:
      print("linkedlist is empty")

Linked = Link()

Linked.add("node1")
Linked.add("node2")
Linked.add("node3")
Linked.add("node4")

Linked.remove("node3")

print(Linked.data)