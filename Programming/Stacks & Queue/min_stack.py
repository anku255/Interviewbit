class MinStack:
  """
    Description::
    Operation       Stack                               Min     Top
    Push(10)        [(10,10)]                           10      (10,10)
    Push(9)         [(10,10), (9,9)]                    9       (9,9)
    Push(11)         [(10,10), (9,9), (11, 9)]          9       (11,9)
    getMin          [(10,10), (9,9), (11, 9)]           9       (9,9)
  """

  def __init__(self):
    self.stack = []

  def push(self, n):
    if len(self.stack) == 0:
      self.stack.append((n, n))
    else:
      currentMin = self.stack[-1][1]
      minimum = min(currentMin, n)
      self.stack.append((n, minimum))

  def pop(self):
    if len(self.stack) == 0:
      return -1

    return self.stack.pop()[0]

  def top(self):
    if self.stack:
      return self.stack[-1][0]
    else:
      return -1

  def getMin(self):
    if len(self.stack) == 0:
      return -1

    return self.stack[-1][1]


s = MinStack()
