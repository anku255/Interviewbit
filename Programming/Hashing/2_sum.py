class Solution:

  def twoSum(self, A, target):
    hashMap = {}  # key: number , val: index + 1
    for i in range(len(A)):
      n = A[i]
      if (target-n) in hashMap:
        return [hashMap[target-n], i+1]

      if n not in hashMap:
        hashMap[n] = i+1
    return []


s = Solution()
A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1,
     9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
print(s.twoSum(A, -3))
