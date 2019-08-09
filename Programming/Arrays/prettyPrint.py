class Solution():
  def prettyPrint(self, A):
    size = 2*A-1
    limit = size
    temp = 0

    result = [[0 for _ in range(size)] for _ in range(size)]

    while A > 0:
      for i in range(temp, limit):
        for j in range(temp, limit):
          result[i][j] = A

      A -= 1
      limit -= 1
      temp += 1

    return result


A = 3

s = Solution()
print(s.prettyPrint(A))
