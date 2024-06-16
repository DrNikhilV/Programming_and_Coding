my_set = {10, 20, 30, 40, 50}

item = 50

if item in my_set:
    my_set.remove(item)
    print("Item present")
    print(my_set)
else:
    print("Item not present")
    print(my_set)