import help_functions as hf

""" Fill in o or x in the blank cells in the below matrix.
    No row, column or diagonal can contain 4 or more o or x in a row"""
#   x   x   _   x   o   x   o   x
#   x   _   _   _   x   _   _   x
#   _   _   o   _   _   _   o   x
#   _   _   _   o   x   x   _   _
#   o   _   x   _   _   _   _   _
#   _   o   _   x   x   x   _   x
#   o   _   o   _   _   _   x   x
#   x   o   o   _   x   _   x   _


def solve_puzzle(grid):
    pass

# Let 0 represent a blank cell, 1 represent 'x' and 2 represent 'o'.
inp_matrix = [[1, 1, 0, 1, 2, 1, 2, 1],
              [1, 0, 0, 0, 1, 0, 0, 1],
              [0, 0, 2, 0, 0, 0, 2, 1],
              [0, 0, 0, 2, 1, 1, 0, 0],
              [2, 0, 1, 0, 0, 0, 0, 0],
              [0, 2, 0, 1, 1, 1, 0, 1],
              [2, 0, 2, 0, 0, 0, 1, 1],
              [1, 2, 2, 0, 1, 0, 1, 0],]

test_matrix = [[1, 1, 1, 1, 2, 1, 2, 1],
               [1, 0, 0, 2, 1, 0, 0, 1],
               [0, 0, 2, 2, 0, 0, 2, 1],
               [0, 2, 0, 2, 1, 1, 1, 0],
               [2, 0, 1, 2, 0, 1, 0, 0],
               [0, 2, 0, 2, 1, 1, 0, 1],
               [2, 0, 2, 0, 1, 0, 1, 1],
               [1, 2, 2, 2, 2, 2, 1, 0],]


test_index = (7, 7)
# print(hf.empty_cells(inp_matrix))
#print(hf.is_grid_valid(inp_matrix))

# row 3, 7
# col 5, 7
# up_right (7, 0), (7,2)
# down right (0,3), (4,0)
# print(f"hf.is_valid({test_index}, test_matrix): {hf.is_valid(4, test_index, test_matrix)}")
# print(f"hf.all_same: {hf.all_same_in_sub_lst([1, 1, 0, 0, 2, 2, 1, 1], 4)}")

empty_indices = hf.empty_cells(inp_matrix)
print(hf.obvious(inp_matrix, empty_indices))




# empty_indices = hf.empty_cells(inp_matrix)
#print(len(empty_indices))
#print(hf.generate_combinations(inp_matrix))