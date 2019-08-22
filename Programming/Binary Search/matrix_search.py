class Solution:
  def searchMatrix(self, A, num):
    m = len(A)
    n = len(A[0])

    low = 0
    high = m * n - 1

    while low <= high:
      mid = (low + high)//2

      row = (mid // n)
      col = mid - row * n
      if A[row][col] == num:
        return 1

      if A[row][col] > num:
        high = mid - 1
      else:
        low = mid + 1
    return 0


A = [
    [1, 3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

s = Solution()

print(s.searchMatrix(A, 20))
