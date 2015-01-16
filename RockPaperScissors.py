from random import randint

def evaluation(user, computer, name):
    if user == computer:
        print("You chose", user, "and computer chose", computer, "!")
        print("This is a draw", end="\n\n")
        outcome["draws"] += 1
    elif user == "ROCK" and computer == "SCISSORS":
        print("You chose", user, "and computer chose", computer, "!")
        print("You win!", end="\n\n")
        outcome["user"] += 1
    elif user == "PAPER" and computer == "ROCK":
        print("You chose", user, "and computer chose", computer, "!")
        print("You win!", end="\n\n")
        outcome["user"] += 1
    elif user == "SCISSORS" and computer == "PAPER":
        print("You chose", user, "and computer chose", computer, "!")
        print("You win!", end="\n\n")
        outcome["user"] += 1
    else:
        print("You chose", user, "and computer chose", computer, "!")
        print("The computer has won!", end="\n\n")
        outcome["computer"] += 1

def game(rounds, name):
    options = ["ROCK", "PAPER", "SCISSORS"]
    while rounds > 0:
        user = input("What do you choose? ROCK, PAPER, or SCISSORS? ")
        computer = options[randint(0, 2)]
        evaluation(user.upper(), computer, name)
        rounds -= 1
        

print("Welcome! Let's play ROCK, PAPER, SCISSORS!")
name = input("Please enter your name ")
rounds = int(input("Please enter the number of games to play "))
print()
outcome = {"user":0, "draws":0, "computer":0}

game(rounds, name)

print("After", rounds, "rounds the results are:")
print("User wins:", outcome["user"], "Computer wins:", outcome["computer"], "Draws:", outcome["draws"])
print()
input("Press enter to exit")
