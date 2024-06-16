cars = {"bmw","honda","benz","audi"}

print(cars)

for car in cars:
    print(f"Cars - {car}")

l = list(cars)
l.remove("honda")
cars = set(l)
print(cars)