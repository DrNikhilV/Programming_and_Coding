numbers_list = [1, 5, 3, 9, 2, 8, 6]

number = set()

max = float('-inf')
num1, num2 = None, None

for num in numbers_list:
    for other_num in number:
        product = num * other_num
        if product > max:
            max = product
            num1, num2 = num, other_num

    number.add(num)

print(f"The two numbers with the maximum product are {num1} and {num2}.")
print(f"The maximum product is {max}.")
