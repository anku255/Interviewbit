class Solution:

  def isPalindrome(self, N):
    return int(str(N) == str(N)[::-1]) # int(True) => 1 , int(False) => 0



s = Solution()

print s.isPalindrome(12212)