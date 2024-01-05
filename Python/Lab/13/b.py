with open("one.txt","a") as file:
    data = " Nikhil"
    file.write(data)

with open("one.txt","r") as file:
    data = file.read()
    print(data)