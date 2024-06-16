numbers_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7]

modified_list = [num for num in numbers_list if num != 0] + [0] * numbers_list.count(0)

print(modified_list)
