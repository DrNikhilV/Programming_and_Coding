m = int(input("Enter the number of floors: "))
n = int(input("Enter the number of rooms: "))

floor = [[1 for i in range(n)] for i in range(m)]

print("Enter the status of each room (1 - dirty, 0 - clean):")
for i in range(m):
    for j in range(n):
        floor[i][j] = int(input(f"Status for room ({i}, {j}): "))

performance = 0

for i in range(m):
    for j in range(n):
        if floor[i][j] == 1:
            print("Cleaning room ({}, {})".format(i, j))
            floor[i][j] = 0
            performance += 1
        if j < n - 1:
            print("Moving to room ({}, {})".format(i, j + 1))

print("\nFinal floor grid after cleaning:")
for row in floor:
    print(*row)
print(f"Performance measure: {performance}")
