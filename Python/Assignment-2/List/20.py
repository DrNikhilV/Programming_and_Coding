list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['b', 'c', 'a', 'g', 'h']

missing_values = list(set(list1) - set(list2))
additional_values = list(set(list2) - set(list1))

print(missing_values)
print(additional_values)
