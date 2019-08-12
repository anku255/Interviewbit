class Solution:

  def intersect(self, A, B):
    i = 0
    j = 0
    result = []
    while i < len(A) and j < len(B):
      if A[i] < B[j]:
        i += 1
      elif A[i] > B[j]:
        j += 1
      else:
        result.append(A[i])
        i += 1
        j += 1

    return result


A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5, 6, 8]


s = Solution()

print(s.intersection(A, B))
