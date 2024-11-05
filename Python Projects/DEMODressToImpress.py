import time

print("Welcome to Dress to Impress")
print("Loading...")
time.sleep(3)
print("INSTRUCTIONS!! Anything within parentheses is what you are picking from and typing.")

while True:
    obj = input("Do you want to dress up a male or a female (male/female or q to quit): ").lower()
    
    if obj == "q":
        print("Exiting the program. Goodbye!")
        break
    elif obj == "female":
        print("Great choice. Let's load your lady.")
        print("Loading...")
        time.sleep(2)
        
        # Hair or face
        while True:
            faHair = input("Do you want to wash your face or do your hair: (face/hair) ").lower()
            if faHair == "face":
                print("Face washed! You look clean!")
                break
            elif faHair == "hair":
                print("Hair done!")
                break
            else:
                print("Invalid choice, please choose again.")
        
        # Makeup and clothing
        print("Let's continue!")
        makeup = input("Do makeup: (makeup) ").lower()
        print("Makeup Done! You are looking good.")

        while True:
            shirDress = input("What next, shirt or dress: (shirt/dress) ").lower()
            if shirDress == "shirt":
                trouSkirt = input("Trousers or skirt: (trousers/skirt) ").lower()
                heBoots = input("Heels or boots: (heels/boots) ").lower()
                print("Finish dress-up. Spray perfume.")
                break
            elif shirDress == "dress":
                heBoots = input("Heels or boots: (heels/boots) ").lower()
                print("Finish dress-up. Spray perfume.")
                break
            else:
                print("Invalid choice, please choose again.")
        
        obj = input("Enter male or female to go again or q to quit: ").lower()
        if obj == "q":
            print("Exiting the program. Goodbye!")
            break
    
    elif obj == "male":
        print("Male dressing sequence not implemented yet.")
    else:
        print("Invalid input, please choose 'male', 'female', or 'q' to quit.")
        
print("YOU LOOK PRETTY!")
