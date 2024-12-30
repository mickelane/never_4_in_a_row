""" This program solves the following puzzle:
    Fill in o or x in the blank cells in a given matrix.
    No row, column or diagonal can contain 4 or more o or x in a row.
    This solution is not very effective. Many calculations must be done. """

#   x   x   _   x   o   x   o   x
#   x   _   _   _   x   _   _   x
#   _   _   o   _   _   _   o   x
#   _   _   _   o   x   x   _   _
#   o   _   x   _   _   _   _   _
#   _   o   _   x   x   x   _   x
#   o   _   o   _   _   _   x   x
#   x   o   o   _   x   _   x   _


import help_functions as hf
import copy


# Let 0 represent a blank cell, 1 represent 'x' and 2 represent 'o'.
# Another example:
yt_input = [[1, 0, 1, 1, 2, 1, 0, 0],
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


print("yt_input:")
hf.print_grid(yt_input)

# Build a whole grid based on the generated combinations.
obv1 = hf.obvious(4, yt_input)
start_attempt_grid = copy.deepcopy(obv1)
empty_indices = hf.empty_cells(obv1)
tries = hf.generate_combinations(empty_indices)
number_of_combinations_done = 0

while number_of_combinations_done < len(tries):
    attempt_grid = start_attempt_grid
    for i, index in enumerate(empty_indices):
        attempt_grid[index[0]][index[1]] = tries[number_of_combinations_done][i]

    if hf.is_grid_valid(4, attempt_grid):
        solution = attempt_grid
        print(f"number of attempts: {number_of_combinations_done + 1}")
        print(f"solution:")
        hf.print_grid(attempt_grid)
        break
    number_of_combinations_done += 1










