def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [int(x) for x in input(f"Enter values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Enter the values.")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 integer values for each row.")
            return enter_matrix()
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

print("Enter values for the first matrix:")
matrix1 = enter_matrix()

print("\nEnter values for the second matrix:")
matrix2 = enter_matrix()

result_matrix = multiply_matrices(matrix1, matrix2)

print("\nProduct of the two matrices:")
print_matrix(result_matrix)
