tuples_list = [(1, 5), (2, 3), (3, 1), (4, 7), (5, 2)]

smallest_tuple = min(tuples_list, key=lambda t: t[1])

print(smallest_tuple)
