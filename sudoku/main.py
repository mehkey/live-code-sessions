'''



Backtracking

left to right
top to bottom

for each . in the matrix

get all possible numbers that are valid for that spot
 
try each number in that spot and move to the next spot
  
if we run into a space that has no valid numbers left, then backtrack
  and try something else
  


'''

# 4
# 3
def is_valid_for_sub_board(board, number, i, j):
  starting_i = (i // 3) * 3
  starting_j = (j // 3) * 3

  for offset_i in range(3):
    for offset_j in range(3):
      if board[starting_i + offset_i][starting_j + offset_j] == number:
        return False
  return True
  

def is_valid_for_column(board, number, i, j):
  for index in range(9):
    num_in_column = board[index][j]
    if num_in_column == number:
      return False
  return True

def is_valid_for_row(board, number, i, j):
  for index in range(9):
    num_in_column = board[i][index]
    if num_in_column == number:
      return False
  return True

def num_is_valid(board, number, i, j):
  return is_valid_for_row(board, number, i, j) and is_valid_for_column(board, number, i, j) and is_valid_for_sub_board(board, number, i, j)

def get_valid_nums_for_index(board, i, j):
  valid_numbers = set()
  for number in range(1, 10):
      if num_is_valid(board, number, i, j):
        valid_numbers.add(str(number))
  return valid_numbers


def sudoku_solve(board):

  def sudoku_recursion(i,j):
    if j == 9:
      j = 0
      i += 1
    if i == 9:
      print("is true")
      print(board)
      return True
    
    if board[i][j] != ".":
      return sudoku_recursion(i,j + 1)
    
    valid_numbers = get_valid_nums_for_index(board, i, j)
    for num in valid_numbers:
      board[i][j] = num
      result = sudoku_recursion(i,j + 1)
      if result:
        return True
      
    board[i][j] = "."
    return False
  print(board)
  return sudoku_recursion(0,0)





'''



Loop throuth all numbers in matrix

   
   
   if not number is not '.':
   
    Loop through 1 to 9:
      
      cur = 1
      pos = [x,y]
      
      set value in array
      
      if sudoku_solve() :
        return True
        
      else:
      
        value and try the next one

    return False
      
   
      
    
      row_check()

      column_check()

      3x3_check for the number()
      
   
   O( 9 * 9 * 9 * 9 36). grid. = (9)^(NxX ) or (9)^(NxX )


def sudoku_solve(board):
  #M = 9
  #N = 9 
  for i in range(9):
    for j in range(9):
      
      if board[i][j] == '.':
        
        for k in "123456789":

          if check_row(board,k,i,j) or check_col(board,k,i,j) or check_3_by_3(board,k,i,j) :
            continue
            
          board[i][j] = k

          if sudoku_solve(board):
            return True
          
          board[i][j] = '.'
        
        return False
    
  return True

def check_row(board,new_val,i,j):
  
  for k in range(9):
    if board[k][j] == new_val:
      return True
  return False

def check_col(board,new_val,i,j):
  
  for k in range(9):
    if board[i][k] == new_val:
      return True
  return False

def check_3_by_3(board,new_val,i,j):
  ni=i//3 * 3
  nj=j//3 * 3

  for x in range(3):
    for y in range(3):
      if board[x+ni][y+nj] == new_val:
        return True

  return False
'''