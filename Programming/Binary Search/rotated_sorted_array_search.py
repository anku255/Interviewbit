class Solution:
  """ 
    Hint:
    One half the array will always be sorted.
    If B doesn't belong to that half, it is in the other half.
   """

  def search(self, A, B):

    low = 0
    high = len(A) - 1

    while low <= high:
      mid = low + (high - low) // 2

      if A[mid] == B:
        return mid

      if A[low] <= A[mid]:

        if A[low] <= B and B <= A[mid]:
          high = mid - 1
        else:
          low = mid + 1
      elif A[mid] <= A[high]:

        if A[mid] <= B and B <= A[high]:
          low = mid + 1
        else:
          high = mid - 1

    return -1


s = Solution()

A = [4, 5, 6, 7, 0, 1, 2]

print(s.search(A, 0))
