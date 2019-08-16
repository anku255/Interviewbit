class Solution:

  def singleNumber(self, A):
    sinlgeNumber = A[0]
    for i in range(1, len(A)):
      sinlgeNumber = sinlgeNumber ^ A[i]

    return sinlgeNumber


A = [1, 2, 3, 4, 4, 3, 1, 2, 7, 7, 11]
s = Solution()
print(s.singleNumber(A))
