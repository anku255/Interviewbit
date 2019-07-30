from __future__ import print_function

class Solution:

  def isMultipleOf3(self, N):
    return N%3 == 0

  def isMultipleOf5(self, N):
    return N%5 == 0

  def isMultipleOf3And5(self, N):
    return self.isMultipleOf3(N) and self.isMultipleOf5(N)

  def findString(self, N):
    if self.isMultipleOf3And5(N):
      return "FizzBuzz"
    elif self.isMultipleOf5(N):
      return "Buzz"
    elif self.isMultipleOf3(N):
      return "Fizz"
    else:
      return N


  def fizzBuzz(self, N):
    arrayOfNums = range(1, N+1)
    return map(self.findString, arrayOfNums)
