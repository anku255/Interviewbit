class Solution:

  def transpose(self, A):
    size = len(A)
    for i in range(size):
      for j in range(i, size):
        A[i][j], A[j][i] = A[j][i], A[i][j]


  def reverseRow(self, A, row):
    i = 0
    j = len(A) - 1

    while i<j:
      A[row][i], A[row][j] = A[row][j] ,A[row][i]
      i += 1
      j -= 1

  def rotate(self, A):
    # Transpose the matrix
    self.transpose(A)

    # reverse each row
    for row in range(len(A)):
      self.reverseRow(A, row)
    return A





matrix = [[1,2 ,3], [4, 5, 6], [7, 8, 9]]

solution = Solution()
print solution.rotateBy90Degrees(matrix)




