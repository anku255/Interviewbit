class Interval():
  def __init__(self, start, end):
    self.start = start
    self.end = end


class Solution():

  def merge(self, A):
    A = sorted(A, key=lambda x: x.start)
    result = [A[0]]

    for i in range(1, len(A)):
      prev = result[-1]
      current = A[i]
      if current.start <= prev.end:
        result.pop()
        newInterval = Interval(prev.start, max(prev.end, current.end))
        result.append(newInterval)
      else:
        result.append(current)

    return result

  '''Solution using list of tuples/lists'''

  # class Solution():

  #   def merge(self, A):
  #     A = sorted(A, key=lambda x: x[0])
  #     result = [A[0]]

  #     for i in range(1, len(A)):
  #       prev = result[-1]
  #       current = A[i]
  #       if current[0] <= prev[1]:
  #         result.pop()
  #         newInterval = (prev[0], max(prev[1], current[1]))
  #         result.append(newInterval)
  #       else:
  #         result.append(current)

  #     return result
