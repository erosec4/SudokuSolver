def find_next_empty(puzzle):
    # finds the index of next unfilled row, col
    # returns row, col tuple or (None, None)
    for r in range(9): # 0-8 indices
        for c in range(9):
            if puzzle[r][c] == -1: # -1 are open spaces
                return r, c
              
    return None, None

def is_valid(puzzle, guess, row, col):
    # determines if guess is valid (true) or not (false)
    # row check:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # column check:
    '''col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])''' #OR:
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # 3 x 3 square check:
    row_start = (row // 3) * 3 # gets first row index bc 1 // 3 = 0, 4 // 3 = 1, 7 // 3 = 2
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
              
    return True #passed all checks


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle) # choose somewhere on puzzle to make a guess
    if row is None:
        return True # true = done. If func returned None tuple, the puzzle is done
        
    for guess in range(1, 10): # make a number guess and check
        if is_valid(puzzle, guess, row, col): # valid guess
            puzzle[row][col] = guess # place guess
            # recurse using this puzzle!
            if solve_sudoku(puzzle):
                return True 
              
        puzzle[row][col] = -1 # invalid guess, so reset and move on
        
    return False # unsolvable

if __name__ == '__main__':
    example_board = [
        [5, 3, -1,    -1, 7, -1,    -1, -1, -1],
        [6, -1, -1,    1, 9, 5,    -1, -1, -1],
        [-1, 9, 8,    -1, -1, -1,    -1, 6, -1],
            
        [8, -1, -1,    -1, 6, -1,    -1, -1, 3],
        [4, -1, -1,    8, -1, 3,    -1, -1, 1],
        [7, -1, -1,    -1, 2, -1,    -1, -1, 6],
            
        [-1, 6, -1,    -1, -1, -1,    2, 8, -1],
        [-1, -1, -1,    4, 1, 9,    -1, -1, 5],
        [-1, -1, -1,    -1, 8, -1,    -1, 7, 9]
      ]
        
    print(solve_sudoku(example_board))
    print(example_board)
