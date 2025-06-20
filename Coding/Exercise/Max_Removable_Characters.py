def is_subsequence(s, p):
    i = j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            j += 1
        i += 1
    return j == len(p)

def max_removals(s, p, removable):
    l, r = 0, len(removable)
    res = 0
    while l <= r:
        mid = (l + r) // 2
        temp = list(s)
        for i in range(mid):
            temp[removable[i]] = ''
        if is_subsequence(''.join(temp), p):
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

print(max_removals("abcacb", "ab", [3,1,0]))