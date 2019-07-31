class Solution:

  def rearrangeArr(self, A):
    n = len(A)

    for i in range(n):
      A[i] = A[i] + (A[A[i]] % n )*n

    for i in range(n):
      A[i] = A[i] / n

    return A


s = Solution()

print s.rearrangeArr([1, 0, 1])