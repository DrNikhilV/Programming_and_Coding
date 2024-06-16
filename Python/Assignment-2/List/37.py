dicts_list1 = [{}, {}, {}]
dicts_list2 = [{1, 2}, {}, {}]

are_all_empty1 = all(not d for d in dicts_list1)
are_all_empty2 = all(not d for d in dicts_list2)

print("Are all dictionaries in the first list empty?", are_all_empty1)
print("Are all dictionaries in the second list empty?", are_all_empty2)
