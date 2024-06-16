my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

key_to_count = 'b'

value_count = list(my_dict.values()).count(my_dict[key_to_count])

print("Number of values associated with key 'b':", value_count)
