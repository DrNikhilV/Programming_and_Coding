def find_max_length(nums):
    count = {0: -1}
    max_len = 0
    s = 0
    for i, num in enumerate(nums):
        s += 1 if num == 1 else -1
        if s in count:
            max_len = max(max_len, i - count[s])
        else:
            count[s] = i
    return max_len

print(find_max_length([0,1,0,1]))