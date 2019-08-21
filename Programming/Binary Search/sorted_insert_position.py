class Solution:

  def searchInsert(self, A, num):
    size = len(A)
    low = 0
    high = size - 1

    while low <= high:
      mid = (low + high)//2
      if A[mid] == num:
        return mid

      if A[mid] > num:
        high = mid - 1
      else:
        low = mid + 1

    return low


s = Solution()

print(s.searchInsert([1, 3, 5, 6], 7))
