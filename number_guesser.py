import random
#r = random.randrange(-5,10) # don't consider 10
# random.randint(-5,10)     #includes 10
#print(r)

top_of_range = input("Enter upper limit: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_number = random.randint(0,top_of_range)
#print(random_number)
guesses = 0
while True:
    guesses+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue # starts from starting of the loop again
    if user_guess == random_number:
        print(f"The actual value is {random_number} and you got it in the {guesses} guesses!")
        break
    else:
        #print("You got it wrong!")
        if guesses == 5:
            print(f"You lost it! The correct answer is {random_number}")
            break
        elif user_guess > random_number:
            print("Your guess is higher than the actual value!")
        else:
            print("Your guess is lower than the actual value!")



