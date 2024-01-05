my_list = ["listen", "silent", "enlist", "tinsel", "apple", "banana", "elbow", "below"]


anagrams = {}

for word in my_list:
    sort = "".join(sorted(word))
    if sort in anagrams:
        anagrams[sort].append(word)
    else:
        anagrams[sort] = [word]

print("Anagram groups:")
for group in anagrams.values():
    print(group)
