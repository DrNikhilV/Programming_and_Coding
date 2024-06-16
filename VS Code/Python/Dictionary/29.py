my_dict = {'key 1': 10, 'key 2': 20, 'key 3': 30}

my_dict_no_spaces = {key.replace(' ', ''): value for key, value in my_dict.items()}

print("Dictionary with keys without spaces:", my_dict_no_spaces)
