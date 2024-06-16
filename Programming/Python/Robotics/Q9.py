def elementwise_multiply(matrix1, matrix2):
    if len(matrix1) != 4 or any(len(row) != 4 for row in matrix1) or \
       len(matrix2) != 4 or any(len(row) != 4 for row in matrix2):
        raise ValueError("Both matrices must be 4x4 matrices.")

    result_matrix = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            result_matrix[i][j] = matrix1[i][j] * matrix2[i][j]

    return result_matrix

def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [float(x) for x in input(f"Enter values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Enter values :")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 values for each row.")
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

result_matrix = elementwise_multiply(matrix1, matrix2)

print("\nElement-wise Multiplication:")
print_matrix(result_matrix)
