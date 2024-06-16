numbers_list = [10, 20, 30, 40, 50, 60]

specified_number = 30

greater_values = [num for num in numbers_list if num > specified_number]

print("Values greater than", specified_number, ":", greater_values)
