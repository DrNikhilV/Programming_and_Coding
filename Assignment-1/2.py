print("1. Celcius to Fahrenheit \n2. Fahrenheit to Celcius")
choice = int(input("Enter choice: "))
if choice == 1:
    c = int(input("Enter celcius: "))
    f = c*9/5+32
    print(c, "C = ", int(f), "F")
    
else:
    f = int(input("Enter fahrenheit: "))
    c = (f-32)*(5/9)
    print(f, "F = ", int(c), "C")