def sudoku_solve(board):
  
  '''
  
  Sudoku Solver: 
  
  9x9 return True if there exists a Sudoku solution,
   return False Otherwise
   
  
  How do we know?
  
  Approach: Backtracking
  
  Try to fill the number 1 to 9 until everything is full
  
  If we can't fill up, return False
  
  If there there is a mistach in row ( same number on the row)
  If there there is a mistach in column 
  If there there is a mistach in box(3x3) 
  Return False
  
  And try anther number
  
  81 cell
  9 * 9 * ... * 9
  
  9^81
  
  O(9^81) (won't have 81 , average case will not try 9 numbers)
  
  
  '''
  solver = SudokuSolver(board)
  
  return solver.is_sudoku_board_solvable()
  
class SudokuSolver:
  
  def __init__(self,board):
    self.board = board
    
  def is_sudoku_board_solvable(self):
    
    #try to fill up the board
    for row in range(9):
      for col in range(9):
        
        if self.board[row][col] == '.':
          
          #try to fill up numbers 1 to 9
          for num in "123456789":
            
            #check if it's valid
            if not self.is_row_valid(row,num):
              #skip
              continue
  
            if not self.is_col_valid(col,num):
              #skip
              continue
            
            if not self.is_box_valid(row,col,num):
              #skip
              continue
            
            
            self.board[row][col] = num
            
            # we fill up one cell, keep goin
            if self.is_sudoku_board_solvable():
              return True
            else:
              # in backtrack, if the sodoku wasnt valid, reset the number to '.' 
              self.board[row][col] = '.'

          # we tried to fill numbers 1 to 9 and failed, return False
          return False
    
    # all the cells have numbers, return True 
    return True
  
  def is_row_valid(self,row,num):
    
    for col in range(0,9):
      if self.board[row][col] == num:
        return False
    
    return True
    
  def is_col_valid(self,col,num):
    for row in range(0,9):
      if self.board[row][col] == num:
        return False
    
    return True
    
  def is_box_valid(self,row,col,num):
    box_row = (row // 3) * 3 #0...9 -> 0 or 1 or 2 -> 0 3 6
    box_col = (col // 3) * 3
    
    for row_x in range(box_row,box_row+3):
      for col_x in range(box_col,box_col+3):
        if self.board[row_x][col_x] == num:
          return False
    
    return True

      
  