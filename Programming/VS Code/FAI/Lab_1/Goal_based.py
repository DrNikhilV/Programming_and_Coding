import random

def generate_matrix(r, c):
    return [[random.randint(0, 9) for i in range(c)] for i in range(r)]

def find_number(matrix, find):
    for i, row in enumerate(matrix):
        if find in row:
            return i, row.index(find)
    return None

def main():
    r = random.randint(2, 5)  
    c = random.randint(2, 5) 
    print("Size of the Matrix :",(r, c))

    matrix = generate_matrix(r, c)

    find = 1 
    result = find_number(matrix, find)

    if result:
        row, col = result
        print(f"Number {find} found at ({row}, {col}).")
    else:
        print(f"Number {find} not found in the matrix.")

if __name__ == "__main__":
    main()
