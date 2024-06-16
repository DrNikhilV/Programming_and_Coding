def is_identity_matrix(matrix):
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        return False

    for i in range(4):
        for j in range(4):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

def enter_matrix():
    matrix = []
    for i in range(4):
        try:
            row = [int(x) for x in input(f"Enter values for row {i + 1} separated by spaces: ").split()]
        except ValueError:
            print("Enter values.")
            return enter_matrix()
        if len(row) != 4:
            print("Please enter exactly 4 integer values for each row.")
            return enter_matrix()
        matrix.append(row)
    return matrix

print("Enter values for a 4x4 matrix:")
user_matrix = enter_matrix()

is_identity = is_identity_matrix(user_matrix)

print("\nResult:")
if is_identity:
    print("The entered matrix is an identity matrix.")
else:
    print("The entered matrix is not an identity matrix.")
