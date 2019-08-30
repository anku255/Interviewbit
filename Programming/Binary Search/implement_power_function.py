class Solution:

  def pow(self, x, n, d):

    if n == 0:
      return 1 % d

    base = x
    result = 1
    while n > 0:
      if n % 2 == 0:
        base = (base * base) % d
        n = n / 2
      else:
        result = (result * base) % d
        n -= 1

    if result < 0:
      result = (result + d) % d
    return result


s = Solution()
print(s.pow(2, 3, 3))
