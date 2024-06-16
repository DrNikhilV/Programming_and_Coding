strings_list = ['abc', 'xyz', 'aba', '1221']

count = 0

for string in strings_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(count)
