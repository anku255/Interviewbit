class Solution:

  def uniquePaths(self, A, B):
    # A - rows
    # B - columns
    if A == 0 or B == 0:
      return 0

    grid = [[1 for _ in range(B)] for _ in range(A)]

    for i in range(1, A):
      for j in range(1, B):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[A-1][B-1]


s = Solution()

print s.uniquePath(2, 2)