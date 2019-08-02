class Solution:

  def gcd(self, a, b):
    if b != 0:
      return self.gcd(b, a%b)
    return a


s = Solution()

print s.gcd(15, 21)