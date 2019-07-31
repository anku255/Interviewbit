from __future__ import print_function

class Solution:

  # returns 1  for A, 2 for B and so on
  def getSingleColNum(self, col):
    return ord(col) - 64


  def titleToNumber(self, col):
    columnNumber = 0
    colList = list(col)
    colList.reverse()

    for position, char  in enumerate(colList) :
      columnNumber += 26**position * self.getSingleColNum(char)

    print(columnNumber)



s = Solution()

s.findColumnNumber('AAA')