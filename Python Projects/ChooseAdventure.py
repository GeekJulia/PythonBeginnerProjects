import time
name = input("Type your name: ")
print("Welcome", name, "to this adventure")
answer = input("You are on a dirt road. A dead end. Do you want to go left or right? ").lower()

if answer == "left":
    river1 = input("You have come to a river. Walk around it or swim across it. Type walk or swim: ").lower()
    if river1 == "swim":
        print("You swam across and got eaten by an alligator")
    elif river1 == "walk":
        time.sleep(2)
        print("You walked for many miles. Ran out of water. You died")
    else:
        print("Wrong answer. You lose")

elif answer == "right":
    r1 = input(
        "You have come to a bridge. It looks wobbly, do you want to cross it or head back. Type Cross or Back: ").lower()
    if r1 == "back":
        print("You went back but a tiger was waiting for you. You died")

    elif r1 == "cross":
        cross1 = input(
            "You cross the bridge . And you meet a stranger. Do you talk to them? (yes / no): ").lower()
        if cross1 == "yes":
            time.sleep(2)
            print("You talk to stranger. You get GOLD. You WIN!")
        elif cross1 == "no":

            print("You ignored the stranger. They are offended, You LOST!")
        else:
            print("Wrong answer. You lose")
    else:
        print("Wrong answer. You lose")

else:
    print("Wrong answer. You lose")

print("Thank you for trying", name)
print("Goodbye")