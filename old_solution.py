

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




def print_matrix(matrix):
    """ Prints the matrix with characters '_', 'x' and 'o' """
    printed_matrix = []
    for row in matrix:
        row_matrix = []
        for element in row:
            if element == 0:
                row_matrix.append('_')
            elif element == 1:
                row_matrix.append('x')
            elif element == 2:
                row_matrix.append('o')
        printed_matrix.append(row_matrix)
    for row in printed_matrix:
        print(row)


def full_matrix(matrix):
    """ Returns True if matrix is solved, else returns False """
    for row in matrix:
        for element in row:
            if element == 0:
                return False

    return True


def same_elements_three_in_a_row(lst):
    """ Returns True if 3 numbers in the lst are the same (not zeros). """
    """ If list length < 3, return False. """
    """ If not 3 numbers in the lst are not the same return False. """
    unique_numbers = set(lst)
    if len(lst) < 3:
        return False
    elif len(unique_numbers) == 1 and 0 not in unique_numbers:
        return True
    else:
        return False


def create_diagonal_down_right(index, matrix):
    """ Creates a list with the diagonal down and right of the index. """
    matrix_row, matrix_col = index[0], index[1]

    if matrix_row < 5 and matrix_col < 5:
        ret_lst = [matrix[matrix_row + 1][matrix_col + 1],
                   matrix[matrix_row + 2][matrix_col + 2],
                   matrix[matrix_row + 3][matrix_col + 3]]
    elif matrix_row == 7 or matrix_col == 7:
        ret_lst = []
    elif (matrix_row * matrix_col) % 6 == 0 and (matrix_row ==  6 or matrix_col == 6):
        ret_lst = [matrix[matrix_row + 1][matrix_col + 1]]
    else:
        ret_lst = [matrix[matrix_row + 1][matrix_col + 1],
                   matrix[matrix_row + 2][matrix_col + 2]]

    return ret_lst


def create_diagonal_down_left(index, matrix):
    """ Creates a list with the diagonal down and left of the index. """
    matrix_row, matrix_col = index[0], index[1]
    if matrix_row < 5 and matrix_col > 2:
        ret_list = [matrix[matrix_row + 1][matrix_col - 1],
                    matrix[matrix_row + 2][matrix_col - 2],
                    matrix[matrix_row + 3][matrix_col - 3]]
    elif matrix_row == 7 or matrix_col == 0:
        ret_list = []
    elif matrix_row == 6 or matrix_col == 1:
        ret_list = [matrix[matrix_row + 1][matrix_col - 1]]
    else:
        ret_list = [matrix[matrix_row + 1][matrix_col - 1],
                    matrix[matrix_row + 2][matrix_col - 2]]

    return ret_list


def create_diagonal_up_right(index, matrix):
    """ Creates a list with the diagonal up and right of the index. """
    matrix_row, matrix_col = index[0], index[1]
    if matrix_row > 2 and matrix_col < 5:
        ret_list = [matrix[matrix_row - 1][matrix_col + 1],
                    matrix[matrix_row - 2][matrix_col + 2],
                    matrix[matrix_row - 3][matrix_col + 3]]
    elif matrix_row == 0 or matrix_col == 7:
        ret_list = []
    elif matrix_row == 1 or matrix_col == 6:
        ret_list = [matrix[matrix_row - 1][matrix_col + 1]]
    else:
        ret_list = [matrix[matrix_row - 1][matrix_col + 1],
                    matrix[matrix_row - 2][matrix_col + 2]]

    return ret_list


def create_diagonal_up_left(index, matrix):
    matrix_row, matrix_col = index[0], index[1]
    if matrix_row > 2 and matrix_col > 2:
        ret_list = [matrix[matrix_row - 1][matrix_col - 1],
                    matrix[matrix_row - 2][matrix_col - 2],
                    matrix[matrix_row - 3][matrix_col - 3]]
    elif matrix_row == 0 or matrix_col == 0:
        ret_list = []
    elif matrix_row == 1 or matrix_col == 1:
        ret_list = [matrix[matrix_row - 1][matrix_col - 1]]
    else:
        ret_list = [matrix[matrix_row - 1][matrix_col - 1],
                    matrix[matrix_row - 2][matrix_col - 2]]

    return ret_list


def three_neighbors(cell_index, matrix):
    """ Scans the rows, columns and diagonals around the cell """
    """ Returns the edited matrix, if conditions are met. Else returns the original matrix  """
    matrix_row, matrix_col = cell_index[0], cell_index[1]

    # Save the True/False answers in a list.
    # Save the neighbor_cells in total_neighbors.

    # Step 1: Check cells to the right or left if there are three of the same in a row.
    three_elements_list, total_neighbours = [], []
    # Check three numbers to the right
    neighbour_cells_to_right = matrix[matrix_row][matrix_col + 1: matrix_col + 4]
    total_neighbours.append(neighbour_cells_to_right)
    print(f"neighbour_cells_to_right: {neighbour_cells_to_right}")
    three_elements_list.append(same_elements_three_in_a_row(neighbour_cells_to_right))

    # Check three numbers to the left
    neighbour_cells_to_left = matrix[matrix_row][max(0, matrix_col - 3):matrix_col]
    total_neighbours.append(neighbour_cells_to_left)
    three_elements_list.append(same_elements_three_in_a_row(neighbour_cells_to_left))
    print(f"neighbour_cells_to_left: {neighbour_cells_to_left}")

    # Step 2: Check cells below and above if there are 3 of the same in a column.
    column_list = []
    for row in matrix:
        column_list.append(row[matrix_col])
    # Check three numbers down
    neighbour_cells_down = column_list[matrix_row + 1: matrix_row + 4]
    total_neighbours.append(neighbour_cells_down)
    three_elements_list.append(same_elements_three_in_a_row(neighbour_cells_down))
    print(f"neighbour_cells_down: {neighbour_cells_down}")
    # Check three numbers up
    neighbour_cells_up = column_list[max(0, matrix_row - 3): matrix_row]
    total_neighbours.append(neighbour_cells_up)
    three_elements_list.append(same_elements_three_in_a_row(neighbour_cells_up))
    print(f"neighbour_cells_up: {neighbour_cells_up}")

    # Step 3: Check diagonals if there are 3 of the same in the diagonal.
    # Check three numbers to the down and right
    neighbor_cells_down_right = create_diagonal_down_right(cell_index, matrix)
    total_neighbours.append(neighbor_cells_down_right)
    print(f"neighbour_cells_down_right: {neighbor_cells_down_right}")
    three_elements_list.append(same_elements_three_in_a_row(neighbor_cells_down_right))
    # Check three numbers to the down and left
    neighbor_cells_down_left = create_diagonal_down_left(cell_index, matrix)
    total_neighbours.append(neighbor_cells_down_left)
    three_elements_list.append(same_elements_three_in_a_row(neighbor_cells_down_left))
    print(f"neighbour_cells_down_left: {neighbor_cells_down_left}")
    # Check three numbers up and to the right
    neighbor_cells_up_right = create_diagonal_up_right(cell_index, matrix)
    total_neighbours.append(neighbor_cells_up_right)
    three_elements_list.append(same_elements_three_in_a_row(neighbor_cells_up_right))
    print(f"neighbor_cells_up_right: {neighbor_cells_up_right}")
    # Check three numbers up and to the left
    neighbor_cells_up_left = create_diagonal_up_left(cell_index, matrix)
    total_neighbours.append(neighbor_cells_up_left)
    three_elements_list.append((same_elements_three_in_a_row(neighbor_cells_up_left)))
    print(f"neighbor_cells_up_left: {neighbor_cells_up_left}")

    print(f"f: three_elements_list: {three_elements_list}")

    # Edit matrice if any neighbor cells are the same (not only zeros) Don't modify already filled cells.
    if True in three_elements_list:
        for element, neighbor_cells in zip(three_elements_list, total_neighbours):
            if element and matrix[matrix_row][matrix_col] == 0:
                if neighbor_cells[0] == 1:
                    matrix[matrix_row][matrix_col] = 2
                elif neighbor_cells[0] == 2:
                    matrix[matrix_row][matrix_col] = 1
                print(f"modified matrix at cell index {matrix_row}, {matrix_col}: New value is {matrix[matrix_row][matrix_col]}")




















    return matrix






def solve_matrix(matrix):
    matrix_solved = False

    #while not matrix_solved:
    for row in matrix:
        for element in matrix:
            # Check for 3 in a row, column or diagonal around the scanned cell
            pass


        matrix_solved = full_matrix(matrix)


    return matrix









# Let 0 represent a blank cell, 1 represent 'x' and 2 represent 'o'.
inp_matrix = [[1, 1, 0, 1, 2, 1, 2, 1],
              [1, 0, 0, 0, 1, 0, 0, 1],
              [0, 0, 2, 0, 0, 0, 2, 1],
              [0, 0, 0, 2, 1, 1, 0, 0],
              [2, 0, 1, 0, 0, 0, 0, 0],
              [0, 2, 0, 1, 1, 1, 0, 1],
              [2, 0, 2, 0, 0, 0, 1, 1],
              [1, 2, 2, 0, 1, 0, 1, 0]]




print("input matrix:")
print_matrix(inp_matrix)


# Debugging
i, j = 5,2

# print(f"three_neighbors_to_right ({i}, {j}): {three_neighbors((i, j), inp_matrix)}")
# lst = [1, 1, 1]
# print(f"same_elements_three_in_a_row({lst}): {same_elements_three_in_a_row(lst)}")
print(f"three_neighbors(({i}, {j}), inp_matrix) {three_neighbors((i, j), inp_matrix)}")
# print(f"create_diagonal_up_left for ({i}, {j}): {create_diagonal_up_left((i, j), inp_matrix)}")

solved_matrix = solve_matrix(inp_matrix)
print("solved matrix:")
print_matrix(solved_matrix)