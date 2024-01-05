my_list = ['a', 'b', 'c', 'd']

nested_dict = current = {}
for key in my_list:
    current[key] = {}
    current = current[key]

print(nested_dict)
