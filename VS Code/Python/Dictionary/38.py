dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

matching_keys = set(dict1.items()) & set(dict2.items())

for key, value in matching_keys:
    print(f"{key}: {value} is present in both x and y")
