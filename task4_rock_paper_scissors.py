# TASK 4 - ROCK, PAPER, SCISSORS GAME (GUI VERSION)
# The user plays against the computer by clicking buttons.
# Score is tracked across rounds.

import tkinter as tk
import random

options = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

user_score = 0
computer_score = 0

# ---- Color palette ----
BG_COLOR = "#1e272e"        # dark charcoal background
TITLE_COLOR = "#00d2d3"     # bright cyan
BUTTON_COLOR = "#576574"    # slate grey for all choice buttons
TEXT_ON_BUTTON = "white"
WIN_COLOR = "#2ecc71"
LOSE_COLOR = "#e74c3c"
TIE_COLOR = "#f1c40f"
SCORE_BG = "#0a3d62"


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result_text = "It's a tie!"
        result_label.config(fg=TIE_COLOR)
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_text = "You win this round!"
        result_label.config(fg=WIN_COLOR)
        user_score += 1
    else:
        result_text = "Computer wins this round!"
        result_label.config(fg=LOSE_COLOR)
        computer_score += 1

    choice_label.config(
        text=emojis[user_choice] + " You  vs  Computer " + emojis[computer_choice]
    )
    result_label.config(text=result_text)
    score_label.config(text="You: " + str(user_score) + "     Computer: " + str(computer_score))


window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("360x400")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="Rock · Paper · Scissors", font=("Arial", 16, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=15)

# Score shown near the top this time, in its own colored bar
score_label = tk.Label(
    window, text="You: 0     Computer: 0", font=("Arial", 12, "bold"),
    bg=SCORE_BG, fg="white", width=30, pady=8
)
score_label.pack(pady=5)

choice_label = tk.Label(window, text="Make your move!", font=("Arial", 12), bg=BG_COLOR, fg="white")
choice_label.pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 13, "bold"), bg=BG_COLOR)
result_label.pack(pady=5)

# Buttons stacked vertically this time instead of side by side
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=15)

tk.Button(
    button_frame, text="🪨 Rock", width=16, font=("Arial", 11, "bold"),
    bg=BUTTON_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("rock")
).pack(pady=4)

tk.Button(
    button_frame, text="📄 Paper", width=16, font=("Arial", 11, "bold"),
    bg=BUTTON_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("paper")
).pack(pady=4)

tk.Button(
    button_frame, text="✂️ Scissors", width=16, font=("Arial", 11, "bold"),
    bg=BUTTON_COLOR, fg=TEXT_ON_BUTTON, command=lambda: play("scissors")
).pack(pady=4)

window.mainloop()
