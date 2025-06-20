def character_replacement(s, k):
    count = [0]*26
    left = max_count = res = 0
    for right in range(len(s)):
        idx = ord(s[right]) - ord('A')
        count[idx] += 1
        max_count = max(max_count, count[idx])
        while (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

print(character_replacement("ABAB", 2))