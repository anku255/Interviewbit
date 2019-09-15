
class Node:
  def __init__(self, data, next=None):
    self.next = next
    self.val = data

  def __repr__(self):
    print('node.val', self.val)

  def __eq__(self, other):
    if self is None and other is None:
      return True
    if self is None or other is None:
      return False
    return self.val == other.val


def traverse(start):
  if start == None:
    print("List is empty")
  else:
    node = start
    while node.next != None:
      print(node.val, end="---->")
      node = node.next
    print(node.val)


class Solution:

  def detectCycle(self, head):
    fast = head
    slow = head

    while fast != None and slow != None:
      fast = fast.next
      if fast == None:
        return None

      fast = fast.next
      slow = slow.next

      if fast == slow:
        break
    if slow != fast:
      return None

    fast = head
    while fast != slow:
      fast = fast.next
      slow = slow.next

    return fast


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head

# traverse(head)
s = Solution()
node = s.detectCycle(head)

print(node.val)
