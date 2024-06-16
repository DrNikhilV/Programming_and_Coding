try:
    a = int(input())
    b = int(input())
    x = a/b
    print(x)

except ZeroDivisionError:
    print("Zero Error")

except Exception as e:
    print(e)

finally:
    print("Finally block")