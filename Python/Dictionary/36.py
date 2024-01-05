from collections import defaultdict

keys_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values_list = [1, 2, 2, 3]

result_dict = defaultdict(set)

for key, value in zip(keys_list, values_list):
    result_dict[key].add(value)

final_dict = dict(result_dict)

print("Dictionary without losing duplicate values:", final_dict)
