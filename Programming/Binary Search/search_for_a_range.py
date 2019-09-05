class Solution:

  # return the first or last occurrence of a number
  # in the array
  def binSearch(self, A, B, range="start"):
    size = len(A)
    low = 0
    high = size - 1

    result = -1

    while low <= high:
      mid = low + (high - low)//2
      if A[mid] == B:
        result = mid
        if range == "end":
          low = mid + 1
        else:
          high = mid - 1

      elif A[mid] > B:
        high = mid - 1
      else:
        low = mid + 1

    return result

  def searchRange(self, A, B):
    startRange = self.binSearch(A, B, range="start")
    endRange = self.binSearch(A, B, range="end")
    return [startRange, endRange]


s = Solution()

print(s.searchRange([5, 7, 7, 8, 8, 10], 5))
