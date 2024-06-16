my_dict = {'fruits': ['apple', 'banana', 'orange'], 'colors': ['red', 'blue', 'green']}

list_item_counts = {key: len(value) for key, value in my_dict.items()}

print("Number of items in each list value:", list_item_counts)
