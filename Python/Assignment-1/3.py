import random

secret_number = random.randint(1, 9)

while True:
    guess = int(input("Guess a number between 1 and 9: "))

    if guess == secret_number:
        print("Well guessed!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
