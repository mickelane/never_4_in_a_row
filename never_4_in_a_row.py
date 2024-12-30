import help_functions as hf
import copy

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

yt_input=   [[1, 0, 1, 1, 2, 1, 0, 0],
             [2, 1, 1, 0, 0, 0, 2, 2],
             [0, 0, 0, 2, 0, 0, 1, 1],
             [1, 2, 0, 0, 2, 0, 2, 0],
             [2, 0, 0, 1, 0, 1, 0, 0],
             [2, 2, 0, 0, 1, 1, 2, 2],
             [1, 1, 2, 0, 0, 2, 0, 1],
             [2, 1, 0, 0, 2, 0, 2, 2],]

yt_solution = [[1, 2, 1, 1, 2, 1, 2, 1],
               [2, 1, 1, 1, 2, 1, 2, 2],
               [1, 2, 2, 2, 1, 2, 1, 1],
               [1, 2, 1, 1, 2, 2, 2, 1],
               [2, 1, 2, 1, 2, 1, 2, 1],
               [2, 2, 2, 1, 1, 1, 2, 2],
               [1, 1, 2, 2, 1, 2, 1, 1],
               [2, 1, 1, 1, 2, 1, 2, 2],]


test_index = (3,6)



# print(hf.empty_cells(inp_matrix))
#print(hf.is_grid_valid(inp_matrix))

# row 3, 7
# col 5, 7
# up_right (7, 0), (7,2)
# down right (0,3), (4,0)
# print(f"hf.is_valid({test_index}, test_matrix): {hf.is_valid(4, test_index, test_matrix)}")
# print(f"hf.all_same: {hf.all_same_in_sub_lst([1, 1, 0, 0, 2, 2, 1, 1], 4)}")

# empty_indices = hf.empty_cells(inp_matrix)
# print(hf.obvious(inp_matrix))
#
# valid = hf.is_valid(1,4, test_index, test_matrix)
# print(valid)


print("yt_input:")
hf.print_grid(yt_input)


print(f"is_grid_valid(4, yt_solution): {hf.is_grid_valid(4, yt_solution)}")

# print(f"empty_indices: {empty_indices}")
# print(f"len(empty_indices): {len(empty_indices)}")





# Build a whole grid based on the combinations.
obv1 = hf.obvious(4, yt_input)
start_attempt_grid = copy.deepcopy(obv1)
empty_indices = hf.empty_cells(obv1)
tries = hf.generate_combinations(empty_indices)
number_of_combinations_done = 0

while number_of_combinations_done < len(tries):
    attempt_grid = start_attempt_grid
    for i, index in enumerate(empty_indices):
        attempt_grid[index[0]][index[1]] = tries[number_of_combinations_done][i]
    print(f"attempt_grid number: {number_of_combinations_done}")
    hf.print_grid(attempt_grid)
    if hf.is_grid_valid(4, attempt_grid):
        print(f"break at: attempt: {number_of_combinations_done}")
        break
    number_of_combinations_done += 1

    ##### Temporary
    if number_of_combinations_done > 9:
        break








# empty_indices = hf.empty_cells(inp_matrix)
#print(len(empty_indices))
#print(hf.generate_combinations(inp_matrix))

