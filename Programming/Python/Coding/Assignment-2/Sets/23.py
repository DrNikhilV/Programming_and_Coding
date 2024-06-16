strings_list = [
    "camera",
    "camel",
    "cameraman",
    "cameroon"
]

min_len = min(len(s) for s in strings_list)

common_prefix = ""

for i in range(min_len):
    char_set = {s[i] for s in strings_list}

    if len(char_set) == 1:
        common_prefix += char_set.pop()
    else:
        break

print("Longest common prefix:", common_prefix)
