from collections import Counter

data_counter = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})

sorted_counter = data_counter.most_common()

print("Sorted Counter by value:", sorted_counter)
