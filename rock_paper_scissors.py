import random
import math
user_score = 0
computer_score = 0

options = ["rock", "paper","scissors"]
count = 0
while count < 5 :
    print(f"round {count+1}")
    user_input = input("Type Rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    print(f"[user: {user_input} ; computer:{options[random_number]}]")
    if options[random_number] != user_input:
        if random_number == 0 and user_input == "scissors":
            print("You won")
            computer_score+=1
        elif random_number == 1 and user_input == "rock":
            print("You won")
            computer_score+=1
        elif random_number == 2 and user_input == "paper":
            print("You won")
            computer_score+=1

        else:
            print("You lost")
            user_score += 1
    count+=1
if user_score > computer_score:
    print("Congratulations asuWIN")
else:
    print("Sorry asuLOST")
