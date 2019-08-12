class Solution:
  def merge(self, A, B):
    i = 0
    j = 0

    while i < len(A) and j < len(B):
      if A[i] < B[j]:
        i += 1
      else:
        A.insert(i, B[j])
        i += 1
        j += 1

    while j < len(B):
      A.append(B[j])
      j += 1

    s = ' '.join(str(x) for x in A) + ' '
    return s


A = [-4, 3]
B = [-2, -2]

s = Solution()
print(s.merge(A, B))
