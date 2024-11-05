import random

user_wins = 0
comp_wins = 0
print("USER VS COMPUTER")
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("Bye")
        break
    
    if user_input not in options :
        print("Invalid")
        continue
    
    random_no = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    comp_pick = options[random_no]
    print("Computer picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        comp_wins += 1


print("User wins:", user_wins, "<---> Computer wins:", comp_wins)
print("GoodBye!")