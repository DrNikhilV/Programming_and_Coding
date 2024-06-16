my_dict = {'a': 2, 'b': 3, 'c': 4}

from functools import reduce
total_product = reduce(lambda x, y: x*y, my_dict.values())

print("Product of all items in the dictionary:", total_product)
