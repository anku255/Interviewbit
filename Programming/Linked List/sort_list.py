
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

  def splitList(self, head):
    slow = head
    fast = head.next

    while fast != None:
      fast = fast.next
      if fast != None:
        slow = slow.next
        fast = fast.next

    left = head
    right = slow.next
    slow.next = None
    return left, right

  def mergeList(self, left, right):
    if left == None:
      return right

    if right == None:
      return left

    head = None

    if left.val < right.val:
      head = left
      head.next = self.mergeList(left.next, right)
    else:
      head = right
      head.next = self.mergeList(left, right.next)

    return head

  def sortList(self, head):
    if head == None or head.next == None:
      return head

    # split the list into two halves
    left, right = self.splitList(head)

    # sort the left and right list
    left = self.sortList(left)
    right = self.sortList(right)

    # merge the left and right halves
    head = self.mergeList(left, right)

    return head


l = LinkedList()
l.add(1)
l.add(2)
l.add(13)
l.add(8)
l.add(11)
l.add(4)
l.add(99)


l.traverse()
s = Solution()
s.sortList(l.start)
l.traverse()
