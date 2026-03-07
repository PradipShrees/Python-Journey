import random

choices = ["s", "r", "p"]

while True:
    player1 = input("Enter s for Scissors, r for Rock, p for Paper --> ").lower().strip()
    if player1 not in choices:
        print("Invalid input. please input s , r or p to play")
        continue

    player2_play = random.choice(choices)

    match (player1, player2_play):
        case ("s", "p"):
            print("My choice was Paper\nYour choice was Scissors\nYou win 🏆")
        case ("p", "r"):
            print("My choice was Rock\nYour choice was Paper\nYou win 🏆")
        case ("r", "s"):
            print("My choice was Scissors\nYour choice was Rock\nYou win 🏆")

        case ("p", "s"):
            print("My choice was Scissors\nYour choice was Paper\nI win 🏆")
        case ("r", "p"):
            print("My choice was Paper\nYour choice was Rock\nI win 🏆")
        case ("s", "r"):
            print("My choice was Rock\nYour choice was Scissors\nI win 🏆")

        case _:
        
            print(f"My choice was {player2_play}\nYour choice was {player1} \nTie 🤨")

    again = input("To continue press y and to stop press n --> ").lower().strip()
    if again != "y":
        break