def calculate_trace(matrix):
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("Input matrix must be a 4x4 matrix.")

    trace = sum(matrix[i][i] for i in range(4))
    return trace

def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [int(x) for x in input(f"Enter integer values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Enter the values.")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 integer values for each row.")
            return enter_matrix()
        matrix.append(row)
    return matrix

print("Enter values for a 4x4 matrix:")
user_matrix = enter_matrix()

matrix_trace = calculate_trace(user_matrix)

print("\nMatrix:")
for row in user_matrix:
    print(row)

print("\nTrace of the Matrix:", matrix_trace)
