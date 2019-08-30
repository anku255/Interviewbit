class Solution:
  def maxSubArray(self, A):
    sumTillNow = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):
      sumTillNow = max(sumTillNow + A[i], A[i])
      if sumTillNow > maxSum:
        maxSum = sumTillNow
    return maxSum


A = [-7, -3, -1, - 5]
s = Solution()
print(s.maxSubArray(A))
