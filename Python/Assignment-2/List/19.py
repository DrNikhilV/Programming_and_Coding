my_list = [0, 1, 2, 3, 4, 5]

modified_list = my_list[:]
for i in range(0, len(my_list) - 1, 2):
    modified_list[i], modified_list[i+1] = modified_list[i+1], modified_list[i]

print(modified_list)
