from __future__ import print_function

'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be afer the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
'''

class Node:
  def __init__(self, data, next=None):
    self.next = next
    self.data = data

  def print(self):
    node = self
    while(node != None):
      print(node.data)
      node = node.next

start = Node(1)
start.next = Node(7)
start.next.next = Node(4)
start.next.next.next = Node(10)
start.next.next.next.next = Node(8)



def Solution(start, val):
  head = start
  tail = start

  node = start

  while node != None:
    nextNode = node.next # taking backup is necessary
    if(node.data < val):
      node.next = head
      head = node
    else:
      tail.next = node
      tail = node

    node = nextNode

  tail.next = None
  return head

head = Solution(start, 5)

head.print()

