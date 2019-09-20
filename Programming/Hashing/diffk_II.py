class Solution:

  def diffPossible(self, A, target):
    hashMap = {}  # key: number , val: True
    for i in range(len(A)):
      n = A[i]
      if (n-target) in hashMap or (n+target) in hashMap:
        return 1

      if n not in hashMap:
        hashMap[n] = True
    return 0


s = Solution()
A = [1, 5, 3]
print(s.diffPossible(A, 4))
