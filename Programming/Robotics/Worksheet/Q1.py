def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [int(x) for x in input(f"Enter integer values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Please enter valid integer values.")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 integer values for each row.")
            return enter_matrix()
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

print("Enter values for the first matrix:")
matrix1 = enter_matrix()

print("\nEnter values for the second matrix:")
matrix2 = enter_matrix()

result_matrix = add_matrices(matrix1, matrix2)

print("\nSum of the two matrices:")
print_matrix(result_matrix)
