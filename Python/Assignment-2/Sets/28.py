import itertools

numbers_list = [1, 2, 3, 4, 5]
target_sum = 9
combinations = []
for combination in itertools.combinations(numbers_list, 3):
    if sum(combination) == target_sum:
        combinations.append(combination)

if combinations:
    print(f"Unique combinations of 3 numbers adding up to {target_sum}:")
    for combination in combinations:
        print(combination)
else:
    print("No unique combinations of 3 numbers add up to the target sum.")
