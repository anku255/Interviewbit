class Solution:

  def reverse(self, N):
    INT_MAX =  2147483647
    INT_MIN = -2147483648

    isNegative = N < 0
    if isNegative:
      N = N*-1
    reversedNum = 0
    while N > 0:
      digit = N % 10
      reversedNum = reversedNum * 10 + digit
      N = N / 10

    if reversedNum > INT_MAX or reversedNum < INT_MIN:
      return 0
    return -reversedNum if isNegative else reversedNum



s = Solution()

print s.reverse(-123)