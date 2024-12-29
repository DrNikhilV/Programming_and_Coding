#Find Minimum Operations to Make All Elements Divisible by Three

def min_ops(arr):
    count = 0
    
    for num in arr:
        rem = num % 3
        if rem == 1:
            count += 1

        elif rem == 2:
            count += 1
    
    return count


array = [1, 2, 3, 4, 5]
result = min_ops(array)
print(result)