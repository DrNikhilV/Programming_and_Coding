data_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = [a + b for a in data_dict['1'] for b in data_dict['2']]

print("All combinations of letters from the dictionary:")
print(*combinations, sep="\n")
