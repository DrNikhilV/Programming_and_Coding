my_dict = {'fruits': [10, 20, 30], 'colors': [5, 15, 25]}

my_dict_summed = {key: sum(value) for key, value in my_dict.items()}

print("Dictionary with values replaced by their sums:", my_dict_summed)
