import copy


def print_grid(grid):
    """ Prints a given grid, replacing the numbers with letters. """
    grid_copy = copy.deepcopy(grid)
    matrix = [[' ' if element == 0 else 'X' if element == 1 else 'o' for element in row] for row in grid_copy]
    for row in matrix:
        print(row)


def all_same_in_sub_lst(lst, len_of_sublist):
    """ Returns True if all elements in any sublist of length len_of_sublist in
        a lst are the same (if elements not all zeros). Else returns False. """
    for i, element in enumerate(lst[0:len(lst) - (len_of_sublist - 1)]):
        sub_lst = lst[i:min(i + len_of_sublist, len(lst))]
        if len(set(sub_lst)) == 1 and 0 not in set(sub_lst) and len(lst) > (len_of_sublist - 1):
            return True

    return False


def empty_cells(grid):
    """ Returns a list with all the indices of all empty cells"""
    empty_cells_lst = []
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == 0:
                empty_cells_lst.append((i, j))
    return empty_cells_lst


def obvious(max_adjacent, grid):
    """ Checks for rows, columns and diagonals that have max_adjacent - 1 in
        a row. If they have max_adjacent - 1 in a row, return a modified grid
        with the opposite number of the number that had three in a row.
        Else return the original grid """
    modified_grid = copy.deepcopy(grid)
    empty_indices_modified_grid = empty_cells(modified_grid)
    not_valid_cells = []
    len1 = len(empty_indices_modified_grid)

    while True:
        len2 = len1
        for index in empty_indices_modified_grid:
            is_cell_valid_one = is_valid(1, 4, index, modified_grid)
            is_cell_valid_two = is_valid(2, 4, index, modified_grid)

            if not is_cell_valid_one:
                modified_grid[index[0]][index[1]] = 2
                empty_indices_modified_grid = empty_cells(modified_grid)
                len2 = len(empty_indices_modified_grid)
                not_valid_cells.append((index[0], index[1]))
            if not is_cell_valid_two:
                modified_grid[index[0]][index[1]] = 1
                empty_indices_modified_grid = empty_cells(modified_grid)
                len2 = len(empty_indices_modified_grid)
                not_valid_cells.append((index[0], index[1]))

        if len1 == len2:
            break

    return modified_grid











def generate_combinations(empty_indices):
    """ Generates combinations of 1s and 2s in the empty cells.
    Returns a list of lists with all combinations"""
    number_of_empty_cells = len(empty_indices)

    # Calculate n as 2^bit_length
    n = 2 ** number_of_empty_cells
    binary_numbers = []

    # Loop through numbers from 0 to n-1
    for i in range(n):
        binary_list = []

        # Convert the number to binary, strip the '0b' prefix, and pad with
        # leading zeros to make it 'bit_length' digits long.
        binary_str = bin(i)[2:].zfill(number_of_empty_cells)

        # Convert the binary string to integers
        for bit in binary_str:
            if bit == '0':
                binary_list.append(1)
            else:
                binary_list.append(2)
        binary_numbers.append(binary_list)

    return binary_numbers



















def is_grid_valid(max_adjacent, grid):
    """ Checks if a whole grid is valid. Returns True if it's valid,
    else returns False """
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if not is_valid(grid[i][j], max_adjacent, (i,j), grid):
                return False

    return True


def is_valid(attempt, max_adjacent, index, grid):
    """ Check if a row, column and diagonals are valid after an attempt for
        the particular index.
        Returns True if it's valid, else returns False.
        """
    test_grid = copy.deepcopy(grid)
    row, col = index[0], index[1]
    num_rows = len(test_grid)
    num_col = len(test_grid[0])
    test_grid[row][col] = attempt

    # Step 1: Check the row
    check_row = test_grid[row]
    if all_same_in_sub_lst(check_row, max_adjacent):
        return False

    # Step 2: Check the column
    check_col = []
    for current_row in test_grid:
        check_col.append(current_row[col])
    if all_same_in_sub_lst(check_col, max_adjacent):
        return False

    # Step 3: Check diagonal from left_up to right_down
    check_diagonal_down_right = []
    start_row = max(row - col, 0)
    start_col = max(col - row, 0)
    i, j = start_row, start_col

    while i < num_rows and j < num_col:
        check_diagonal_down_right.append(test_grid[i][j])
        i += 1
        j += 1

    if all_same_in_sub_lst(check_diagonal_down_right, max_adjacent):
        return False

    # Step 4: Check the diagonal from left_down to right_up
    check_diagonal_up_right = []
    start_row = min(row + col, num_rows - 1)
    start_col = max(row + col - (num_rows - 1), 0)
    i, j = start_row, start_col

    while i >= 0 and j < num_col:
        check_diagonal_up_right.append(test_grid[i][j])
        i -= 1
        j += 1

    if all_same_in_sub_lst(check_diagonal_up_right, max_adjacent):
        return False

    return True








