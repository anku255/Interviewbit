class Solution():
  def sortColors(self, A):
    i = j = 0

    while i < j:
      if A[i] == 0:
        i += 1
      elif A[i] == 2:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    return A


A = [0, 1, 2, 0, 1, 2]
s = Solution()
print(s.sortColors(A))
