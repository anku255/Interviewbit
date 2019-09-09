
class Node:
  def __init__(self, data, next=None):
    self.next = next
    self.val = data

  def __repr__(self):
    print('node.val', self.val)


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

  def traverse(self):
    if self.start == None:
      print("List is empty")
    else:
      node = self.start
      while node.next != None:
        print(node.val, end="---->")
        node = node.next
      print(node.val)