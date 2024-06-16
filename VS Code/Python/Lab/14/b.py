try:
    a = int(input())
    b = int(input())
    x = a / b
    print(x)

except ZeroDivisionError:
    print("Cannot divide by Zero")
    
except Exception as e:
    print(e)

finally:
    print("Finally Block")
