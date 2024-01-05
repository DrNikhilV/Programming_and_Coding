strings_list = ['abcd', 'abc', 'bcd', 'bkie']

specific_char = 'a'

items_starting_with_char = [string for string in strings_list if string.startswith(specific_char)]

print("Items starting with", specific_char, "from the list:", items_starting_with_char)
