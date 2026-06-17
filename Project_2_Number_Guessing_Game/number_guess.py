import random
print("Welcome To The Number Guessing Game!")
number = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100: "))

while guess!=number:
    if guess>number:
        print("Too high!Try again and guess lowr")
    else:
        print("Too low!Try again and guess higher")
    guess = int(input("Guess a number between 1 and 100: "))
    if guess== number:
        print("Congratulations! You guessed the number correctly!")
        break
