lists_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_lists = [list(x) for x in set(tuple(x) for x in lists_list)]

print(unique_lists)
