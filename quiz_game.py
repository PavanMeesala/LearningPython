print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print("Okay! Let's paly :)")

answer = input("What does CPU stands for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")