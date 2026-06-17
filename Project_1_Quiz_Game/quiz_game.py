print("Welcome To The Quiz Game!")

choice = input("Do you want to play the game?(yes/no)").lower()
if choice!="yes":
    quit()

score = 0

answer = input("What does CPU stand for?").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does GPU stand for?").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RAM stands for?").lower()
if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got "+str(score)+" questions correct!")

print("You got "+str((score/3)*100)+"%")