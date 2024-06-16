import numpy as np

a = []

print("Enter Matrix 1")
for i in range(4):
    lst = []
    for j in range(4):
        n = int(input())
        lst.append(n)
    a.append(lst)

print("Matrix 1")
a = np.array(a)
print(a)
print("\n")

b = np.linalg.inv(a)
print(b)