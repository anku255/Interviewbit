class Solution():

  def setZeroes(self, A):
    
    rows = len(A)
    cols = len(A[0])

    isFirstRowZero = False
    isFirstColZero = False
   
    for col in range(cols):
      if A[0][col] == 0:
        isFirstRowZero = True
        break
    
    for row in range(rows):
      if A[row][0] == 0:
        isFirstColZero = True
        break
  
    for i in range(1, rows):
      for j in range(1, cols):
        if A[i][j] == 0:
          A[i][0]=0
          A[0][j]=0
          
    for i in range(1, rows):
      for j in range(1, cols):
         if A[i][0]==0 or A[0][j]==0:
             A[i][j]=0   
          
    if isFirstRowZero:
      for col in range(cols):
        A[0][col] = 0
        
    if isFirstColZero:
      for row in range(rows):
        A[row][0] = 0

    return A


s = Solution()
arr = [[0, 1], [1, 1]]

print(s.setZeroes(arr))
