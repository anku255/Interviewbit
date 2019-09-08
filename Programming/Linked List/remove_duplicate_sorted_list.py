
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


class Solution:

  def deleteDuplicates(self, head):
    if head == None:
      return None

    currentNode = head
    nextNode = head.next

    while nextNode != None:
      while nextNode and currentNode.val == nextNode.val:
        currentNode.next = nextNode.next
        nextNode = nextNode.next

      currentNode = currentNode.next

    return head


l = LinkedList()
l.add(1)
l.add(2)
l.add(2)
l.add(2)
l.add(2)
l.add(3)
l.add(3)
l.add(4)
l.add(4)
l.add(4)

s = Solution()
s.deleteDuplicates(l.start)

l.traverse()
