def generate_diagonal_matrix(values):
    if len(values) != 4:
        raise ValueError("Emter 4 values for the diagonal matrix.")

    diagonal_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        diagonal_matrix[i][i] = values[i]

    return diagonal_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

try:
    diagonal_values = [float(x) for x in input("Enter 4 values for the diagonal matrix separated by spaces: ").split()]
except ValueError:
    print("Enter values: ")
    exit()

diagonal_matrix = generate_diagonal_matrix(diagonal_values)

print("\nDiagonal Matrix:")
print_matrix(diagonal_matrix)
