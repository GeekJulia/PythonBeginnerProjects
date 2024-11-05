import time
print("Welcome to my computer quiz")
points = 0
ques = 0
time.sleep(1)
print("First question: 2 points")
time.sleep(1)
print("Second question: 2 points")
time.sleep(1)
print("Third question: 3 points")
time.sleep(1)
print("Fourth question: 5 points")
while True:
    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        quit()
    print("Okay let's play:) ")

    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        points += 2
        ques += 1
    else:
        print("Incorrect!")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        points += 2
        ques += 1
    else:
        print("Incorrect!")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        points += 3
        ques += 1
    else:
        print("Incorrect!")

    answer = input("what does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct!")
        points += 5
        ques += 1
    else:
        print("Incorrect!")

    print(f"You got {ques} questions correct")
    print (f"Total of {points} points.")
    print("Percentage:"+ str((ques/4) * 100) + "%." )
    points = 0
    ques = 0


