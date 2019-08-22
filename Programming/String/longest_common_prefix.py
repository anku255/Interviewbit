class Solution:

  def longestCommonPrefix(self, A):

    minLength = len(A[0])

    for string in A:
      if len(string) < minLength:
        minLength = len(string)

    for j in range(minLength):
      prev = ''
      for i in range(len(A)):
        if i == 0:
          prev = A[i][j]
          continue

        if A[i][j] != prev:
          return A[i][0:j]

    return A[0][0:minLength]


s = Solution()
A = ["geeksforgeeks", "geek", "geekr", "geek"]
print(s.longestCommonPrefix(A))
