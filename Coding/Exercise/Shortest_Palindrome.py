def shortest_palindrome(s):
    rev = s[::-1]
    for i in range(len(s)):
        if s.startswith(rev[i:]):
            return rev[:i] + s
    return ""

print(shortest_palindrome("aacecaaa"))