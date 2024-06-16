l = eval(input("Enter an array in format [123,1323,134,52]: "))
d = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
digits = len(str(max(l)))
mod = 10
for i in range(digits):
    new_l = []
    for num in l:
        nl = d[(num % mod) // (mod // 10)]
        nl.append(num)
    for lst in d.values():
        new_l += lst
        lst.clear()
    l = new_l
    mod *= 10
    print("Round", i)
    print(l)