

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

    
