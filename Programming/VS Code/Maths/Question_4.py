def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)

clock1_interval = 3
clock2_interval = 4
clock3_interval = 10

lcm_all_clocks = lcm_of_three(clock1_interval, clock2_interval, clock3_interval)

print("You would hear all clocks ring at the same time again after", lcm_all_clocks, "hours.")