my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

result_pairs = []

seen_elements = set()

for num in my_list:
    complement = target_sum - num
    if complement in seen_elements:
        result_pairs.append((num, complement))
    seen_elements.add(num)

print(f"Pairs with the sum {target_sum}:")
for pair in result_pairs:
    print(pair)
