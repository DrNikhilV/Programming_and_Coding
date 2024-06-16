def transpose_matrix(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [int(x) for x in input(f"Enter integer values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Please enter values.")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 integer values for each row.")
            return enter_matrix()
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

print("Enter values for a 4x4 matrix:")
user_matrix = enter_matrix()

transposed_matrix = transpose_matrix(user_matrix)

print("\nOriginal Matrix:")
print_matrix(user_matrix)

print("\nTransposed Matrix:")
print_matrix(transposed_matrix)
