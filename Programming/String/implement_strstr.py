class Solution:
  def strStr(self, string, query):
    i = 0
    j = 0
    while i < len(string):
      temp = i
      while i < len(string) and j < len(query) and string[i] == query[j]:
        if j == len(query) - 1:
          return temp
        i += 1
        j += 1

      i = temp + 1
      j = 0
    return -1


s = Solution()

print(s.strStr("super", "up"))
