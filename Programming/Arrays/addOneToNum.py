class Solution:

  def plusOne(self, A):
    carry = 0
    A[-1] += 1
    if A[-1] == 10:
      A[-1] = 0
      carry = 1
    for i in range(len(A) - 2, -1, -1):
      A[i] += carry
      if A[i] == 10:
        A[i] = 0
        carry = 1
      else:
        carry = 0
        break

    if carry != 0:
      A.insert(0, 1)

    while A[0] == 0:
      del A[0]

    return A


s = Solution()

A = [9, 9, 9, 9, 9]


print(s.plusOne(A))
