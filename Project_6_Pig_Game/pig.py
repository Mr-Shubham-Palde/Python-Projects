import random
print("Welcome to the pig game!")

def roll():
    dice = random.randint(1,6)
    return dice


while True:
    players = input("Enter the number of players (2-4):")

    if players.isdigit() and 2 <= int(players) <=4:
        players = int(players)
        break
    else:
        print("Invalid input. Enter a number between 2 and 4.")

print(players, "players will play the game.")

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores)< max_score:
    for player_idx in range(players):
        print("\nPlayer ", player_idx+1 ,"Turn has just started")
        print("Your total score is:",player_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("\nDo you want to roll the dice?(y/n):")
            if should_roll.lower() != "y":
                print("You dont want to play")
                break
            
            value = roll()
            if value == 1:
                print("You got 1! your game ends")
                
                break
            else:
                current_score += value
                print("You rolled a:",value)
            
            print("Your Score is:",current_score)
            
        player_scores[player_idx] += current_score
        print("Your total score is: ",player_scores[player_idx])
        print(player_scores)

                

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player Number",winning_idx+1,"has won with Score:",max_score)


