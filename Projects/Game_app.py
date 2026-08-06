# this is not my code , i used chatgpt to generate it. I am still learning it
import tkinter as tk
import random

choices = ["s", "r", "p"]
names = {"s": "Scissors", "r": "Rock", "p": "Paper"}

def play(user_choice: str):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Tie 🤝"
    elif (user_choice, computer_choice) in {("s", "p"), ("p", "r"), ("r", "s")}:
        result = "You win 🏆"
    else:
        result = "I win 🏆"

    output.set(
        f"Your choice: {names[user_choice]}\n"
        f"My choice: {names[computer_choice]}\n"
        f"Result: {result}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")

output = tk.StringVar(value="Choose Rock, Paper, or Scissors to start.")

label = tk.Label(root, textvariable=output, font=("Arial", 14), justify="left", padx=10, pady=10)
label.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=12, command=lambda: play("r")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=12, command=lambda: play("p")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=12, command=lambda: play("s")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Quit", width=12, command=root.destroy).pack(pady=10)

root.mainloop()