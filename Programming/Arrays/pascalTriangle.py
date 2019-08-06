class Solution():
  def pascal(self, numRows):
    if numRows == 0:
      return []

    triangle = [[1]]
    for i in range(1, numRows):
      row = [1]
      for j in range(1, i+1):
        prevRow = triangle[i-1]
        val1 = prevRow[j-1]
        val2 = 0 if len(prevRow) == j else prevRow[j]
        val = val1 + val2
        row.append(val)
      triangle.append(row)
    return triangle


s = Solution()
print(s.pascal(6))
