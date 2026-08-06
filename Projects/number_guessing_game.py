import random
number_to_guess = random.randint(1, 100)
while True:
    try:
        roll = int(input("Guess the number from 1 to 100:-->"))
        if roll > number_to_guess:
            print("Too high !")
        elif roll < number_to_guess:
            print("Too low !")
        else:
            print("Your guessed the right number. Congratulation 🥳")
            break
    except ValueError:
        print("Please enter a whole number like 1,2,3")






