class Solution:

  def atoi(self, A):
    A = A.strip()

    result, i = 0, 0
    sign = 1

    if (A[i] == '+' or A[i] == '-'):
      sign = 1 if A[i] == '+' else -1
      i += 1

    while i < len(A) and ord(A[i]) >= ord('0') and ord(A[i]) <= ord('9'):
      result = result * 10 + ord(A[i]) - ord('0')
      i += 1

    result = result * sign
    INT_MAX = 2**31-1
    INT_MIN = -2**31
    return max(INT_MIN, min(result, INT_MAX))


s = Solution()
print(s.atoi("+7"))
