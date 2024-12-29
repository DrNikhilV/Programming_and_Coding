#Number of Good Pairs

def good_pairs(arr):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    pair_count = 0
    
    for count in frequency.values():
        if count > 1:
            pair_count += (count * (count - 1)) // 2

    return pair_count

array = [1, 2, 3, 1, 2, 1] 
result = good_pairs(array)
print(result)
