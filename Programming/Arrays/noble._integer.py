class Solution:

  def solve(self, A):
    A = sorted(A)
    size = len(A)
    ans = -1
    i = 0

    if size == 0:
      return ans

    while i < size:

      while i + 1 < size and A[i] == A[i + 1]:
        i += 1

      if (size - (i+1) == A[i]):
        ans = 1
        break

      i += 1

    return ans


s = Solution()

print(s.solve([5, 6, 2]))
