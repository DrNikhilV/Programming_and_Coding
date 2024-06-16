#Dot Plot Matrix
s1 = "TAGCC" #TAGCCGC
s2 = "GCCATGC"

l1 = len(s1)
l2 = len(s2)

matrix = []
for i in range(l1):
    row = []
    for j in range(l2):
        if s1[i] == s2[j]:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for i in matrix:
    print(i)


score = 0
for i in range(l1):
    for j in range(l2):
        if i==j:
            if(s1[i] == s2[j]):
                score +=1

print(score)