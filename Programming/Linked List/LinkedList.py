
class Node:
  def __init__(self, data, next=None):
    self.next = next
    self.data = data

  def __repr__(self):
    print('node.data', self.data)


class LinkedList:
  def __init__(self):
    self.start = None

  def add(self, data):
    newNode = Node(data)
    if self.start == None:
      self.start = self.end = newNode
    else:
      node = self.start
      while node.next != None:
        node = node.next
      node.next = newNode
