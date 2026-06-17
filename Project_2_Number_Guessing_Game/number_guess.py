import random
print("Welcome To The Number Guessing Game!")
number = random.randint(1,100)

chance = 5
print("You have total ", chance," Chances to guess the number correctly!")

guess = int(input("Guess a number between 1 and 100: "))

while guess!=number:
    if chance == 0:
        print("Game Over! You have used all your chances. The correct number was", number)
        break
        

    if guess>number:
        chance-=1
        print("Too high!Try again and guess lower", "Chance Remaining",chance)
        
    else:
        chance-=1
        print("Too low!Try again and guess higher", "Chance Remaining",chance)
        
    guess = int(input("Guess a number between 1 and 100: "))

    if guess== number:
        print("Congratulations! You guessed the number correctly!")
        break
    
