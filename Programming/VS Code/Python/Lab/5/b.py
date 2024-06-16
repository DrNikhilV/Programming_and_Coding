a = int(input())
b = int(input())

while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1

print("Sum:", a)