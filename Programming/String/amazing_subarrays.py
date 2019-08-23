class Solution:

  def isVowel(self, A):
    A = A.lower()

    return A == 'a' or A == 'e' or A == 'i' or A == 'o' or A == 'u'

  def solve(self, A):
    count = 0

    for i in range(len(A)):
      if self.isVowel(A[i]):
        count += len(A) - i

    return count


s = Solution()

print(s.solve('ABEA'))
