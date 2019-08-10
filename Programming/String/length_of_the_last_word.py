class Solution:
  def lengthOfLastWord(self, s):
    s = s.strip()
    arr = s.split(' ')
    return len(arr[-1]) if len(arr) else 0


string = "Hello, World"
s = Solution()
print(s.lengthOfLastWord(string))
