class Solution:

  def _findSpecialProduct(self, A, productType="left"):
    stack = []
    product = [0]*len(A)

    indices = range(len(A)) if productType == "left" else range(len(A)-1 , -1, -1)

    for i in indices:
      while stack and A[i] >= A[stack[-1]]:
        stack.pop()

      product[i] = stack[-1] if stack else 0
      stack.append(i)

    return product


  def maxSpecialProduct(self, A):
    leftSpecialProd = self._findSpecialProduct(A)
    rightSpecialProd = self._findSpecialProduct(A, productType="right")

    maxProd = -float('inf')
    for i in range(len(A)):
      maxProd = max(leftSpecialProd[i] * rightSpecialProd[i], maxProd)

    return maxProd % 1000000007

s = Solution()

arr = [43, 5, 3 ,2, 7]

print s.specialProduct(arr)
