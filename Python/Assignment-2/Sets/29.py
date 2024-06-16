my_list = [10, 5, 8, 2, 7, 10, 15, 20]

unique = set(my_list)

sort = sorted(unique, reverse=True)

third_largest = None
if len(sort) >= 3:
    third_largest = sort[2]

if third_largest is not None:
    print(f"The third largest number is: {third_largest}")
else:
    print("There is no third largest number in the list.")
