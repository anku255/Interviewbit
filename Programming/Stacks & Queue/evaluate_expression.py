class Solution:

  def evalRPN(self, A):
    stack = []
    operators = ['+', '-', '*', '/']
    for e in A:
      if e in operators:
        n2 = int(stack.pop())
        n1 = int(stack.pop())

        if e == '+':
          stack.append(n1 + n2)
        elif e == '-':
          stack.append(n1 - n2)
        elif e == '*':
          stack.append(n1 * n2)
        else:
          stack.append(n1 // n2)
      else:
        stack.append(e)

    return stack.pop()


s = Solution()
A = ["4", "13", "5", "/", "+"]
print(s.evalRPN(A))
