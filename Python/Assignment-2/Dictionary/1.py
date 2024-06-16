my_dict = {0: 10, 1: 20, 2: 5, 3: 15}

sorted_dict_asc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

sorted_dict_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

print("Sorted dictionary (ascending):", sorted_dict_asc)
print("Sorted dictionary (descending):", sorted_dict_desc)
