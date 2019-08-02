class Solution:

  def wave(self, A):
    # sort the list
    A.sort()

    for i in range(0, len(A)-1, 2):
      A[i], A[i+1] = A[i+1], A[i]

    return A

s = Solution()

arr = [43, 67]
print s.wave(arr)