class Solution():

  def findMinXor(self, A):
    A.sort()
    minXOR = float('inf')
    val = 0
    for i in range(len(A) - 1):
      val = A[i] ^ A[i + 1]
      minXOR = min(minXOR, val)

    return minXOR


s = Solution()

print(s.findMinXor([0, 4, 9, 7]))
