my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}

unique_dict = {key: value for key, value in my_dict.items() if list(my_dict.values()).count(value) == 1}

print("Dictionary after removing duplicates:", unique_dict)
