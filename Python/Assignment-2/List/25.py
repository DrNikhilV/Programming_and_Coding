strings_list = ['apple', 'apple', 'apple', 'apple']

given_string = 'apple'

are_equal = all(item == given_string for item in strings_list)

print("All items in the list are equal to the given string:", are_equal)
