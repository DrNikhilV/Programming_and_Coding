list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

if set1.intersection(set2):
    print("True")
else:
    print("False")
