data_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 50, 'e': 400}

sorted_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
highest_3_values = dict(sorted_dict[:3])

print(highest_3_values)
