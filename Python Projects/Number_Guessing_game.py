import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Less than or equal to zero.")
        quit()
else:
    print("Not a number.")
    quit()


random_no = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Not a number.")
        continue
    if user_guess == random_no:
        print("You got it!")
        break
    elif user_guess > random_no:
        print("Number is greater.")
    else:
        print("Number is less.")

print("You got it in", guesses, "guesses")