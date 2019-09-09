
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

  def swapPairs(self, head):
    if head == None:
      return head

    curr = head
    nextNode = curr.next
    if nextNode == None:
      return curr

    ans = nextNode
    prev = None

    while curr != None and nextNode != None:
      curr.next = nextNode.next
      nextNode.next = curr

      if prev != None:
        prev.next = nextNode

      prev = curr
      curr = curr.next
      if curr != None:
        nextNode = curr.next

    return ans


def traverse(start):
  if start == None:
    print("List is empty")
  else:
    node = start
    while node.next != None:
      print(node.val, end="---->")
      node = node.next
    print(node.val)


l = LinkedList()
l.add(1)
l.add(2)
l.add(13)
l.add(8)
l.add(11)
l.add(4)

l.traverse()
s = Solution()
h = s.swapPairs(l.start)
traverse(h)
