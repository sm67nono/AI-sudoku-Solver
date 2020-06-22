#A sample 2D matrix for solving -- to be replaced with actual input
matrix = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

SIZE=9

def showSolved():
    for i in matrix:
        print (i)

def checkUnassigned(row, col):
    num_unassign = 0
    for i in range(0,SIZE):
        for j in range (0,SIZE):
            
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def checkSafe(n, r, c):
  
    for i in range(0,SIZE):
       
        if matrix[r][i] == n:
            return False
   
    for i in range(0,SIZE):
        
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
   
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True

#using backtracking log(9^(n*n)) time complexity
def sudokuSolver():
    row = 0
    col = 0
    
    a = checkUnassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
   
    for i in range(1,10):
        
        if checkSafe(i, row, col):
            matrix[row][col] = i
            
            if sudokuSolver():
                return True
          
            matrix[row][col]=0
    return False

if sudokuSolver():
    showSolved()
else:
    print("Solution not Found")
