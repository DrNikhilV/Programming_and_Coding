def double(x):
    return 2 * x

a = [1, 2, 3, 4, 5]
b = list(map(double, a))

print("Original list:", a)
print("Doubled list:", b)
