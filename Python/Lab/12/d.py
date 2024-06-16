with open("one.txt","r") as file:
    a = file.read()

with open("two.txt","r") as file:
    b = file.read()

c = a + b

with open("Three.txt","w") as file:
    file.write(c)
