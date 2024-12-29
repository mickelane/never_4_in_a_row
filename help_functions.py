import copy

def print_grid(grid):
    for row in grid:
        print(row)



def all_same_in_sub_lst(lst, len_of_sublist):
    """ Returns True if all elements in any sublist of length len_of_sublist in
        a lst are the same (if elements not all zeros). Else returns False """
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


def obvious(grid, empty_indices):
    """ Checks for rows, columns and diagonals that have 3 in a row.
        If they have three in a row, return a modified grid with the opposite
        number of the number that had three in a row. Else return the original
        grid """
    modified_grid = copy.deepcopy(grid)
    not_valid_cells = []
    for indices in empty_indices:
        print(f"obvious: empty indices: {indices}")

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if is_valid(3, (i, j), modified_grid):
                pass
            else:
                not_valid_cells.append((i, j))


    return not_valid_cells




def generate_combinations(empty_indices):
    """ Generates combinations of 1s and 2s in the empty cells.
    Returns a list of lists with all combinations"""
    number_of_empty_cell = len(empty_indices)

    # Calculate n as 2^bit_length
    n = 2 ** number_of_empty_cell
    binary_numbers = []

    # Loop through numbers from 0 to n-1
    for i in range(n):
        binary_list = []

        # Convert the number to binary, strip the '0b' prefix, and pad with
        # leading zeros to make it 'bit_length' digits long.
        binary_str = bin(i)[2:].zfill(number_of_empty_cell)

        # Convert the binary string to integers
        for bit in binary_str:
            if bit == 0:
                binary_list.append(1)
            else:
                binary_list.append(2)
        binary_numbers.append(binary_list)

    return binary_numbers



















def is_grid_valid(grid):
    """ Checks if a whole grid is valid. Returns True if it's valid,
    else returns False """
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if not is_valid(4, (i,j), grid):
                return False

    return True


def is_valid(max_adjacent, index, grid):
    """ Check if a row, column and diagonals are valid for the particular index.
    Returns True if it's valid, else returns False.
    """
    test_grid = copy.deepcopy(grid)
    row, col = index[0], index[1]
    num_rows = len(grid)
    num_col = len(grid[0])


    # Step 1: Check the row
    check_row = test_grid[row]
    if all_same_in_sub_lst(check_row, max_adjacent):
        print(f"is_valid: row not valid for index: {index}, {check_row}")
        return False


    # Step 2: Check the column
    check_col = []
    for current_row in test_grid:
        check_col.append(current_row[col])
    if all_same_in_sub_lst(check_col, max_adjacent):
        print(f"is_valid: column not valid for index: {index}, {check_col}")
        return False


    # Step 3: Check diagonal from left_up to right_down
    check_diagonal_down_right = []
    start_row = max(row - col, 0)
    start_col = max(col - row, 0)
    i, j = start_row, start_col

    while i < num_rows and j < num_col:
        check_diagonal_down_right.append(grid[i][j])
        i += 1
        j += 1

    if all_same_in_sub_lst(check_diagonal_down_right, max_adjacent):
        print(f"is_valid: diagonal RIGHT DOWN not valid for index: {index}, {check_diagonal_down_right}")
        return False


    # Step 4: Check the diagonal from left_down to right_up
    check_diagonal_up_right = []
    start_row = min(row + col, num_rows - 1)
    start_col = max(row + col - (num_rows - 1), 0)
    i, j = start_row, start_col

    while i >= 0 and j < num_col :
        check_diagonal_up_right.append(grid[i][j])
        i -= 1
        j += 1

    if all_same_in_sub_lst(check_diagonal_up_right, max_adjacent):
        print(f"is_valid: diagonal RIGHT UP not valid for index: {index}, {check_diagonal_up_right}")
        return False



    return True












