name = "Nikhil"

# Slicing
print(name[::-1])

# One Pointer
rev_name = ""
for i in range(len(name) - 1, -1, -1):
    rev_name += name[i]
print(rev_name)

# Two Pointer (in-place reverse)
name_list = list(name)
left = 0
right = len(name_list) - 1

while left < right:
    name_list[left], name_list[right] = name_list[right], name_list[left]
    left += 1
    right -= 1

inplace_name = "".join(name_list)
print(inplace_name)