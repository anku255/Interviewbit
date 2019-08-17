class Solution:

  def isBitSetAtPos(self, num, pos):
    return True if num & (1 << pos) else False

  def setBitAtPos(self, num, pos):
    return num | (1 << pos)

  def unsetBitAtPos(self, num, pos):
    return num | (0 << pos)

  def singleNumber(self, A):

    result = 0

    # for each 32 positions
    for i in range(32):
      # count the no of 1's at the ith position of elements
      count = 0
      for num in A:
        if self.isBitSetAtPos(num, i):
          count += 1

      # if count of 1's is divisible by 3 then on the ith position
      # of result set bit 0, otherwise 1
      if(count % 3 == 0):
        result = self.unsetBitAtPos(result, i)
      else:
        result = self.setBitAtPos(result, i)

    return result


A = [1, 1, 2, 1, 2, 3, 2, 3, 3, 5]
s = Solution()
print(s.singleNumber(A))
# print(s.setBitAtPos(5, 1))
