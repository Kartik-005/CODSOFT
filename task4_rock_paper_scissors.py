# TASK 4 - ROCK, PAPER, SCISSORS GAME
# The user plays against the computer.
# Score is tracked across rounds until the user quits.

import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("----- ROCK, PAPER, SCISSORS -----")

while True:
    user_choice = input("\nChoose rock, paper, or scissors (or 'quit' to stop): ").lower()

    if user_choice == "quit":
        break

    if user_choice not in options:
        print("Invalid choice. Please type rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score -> You:", user_score, " Computer:", computer_score)

    play_again = input("Play another round? (y/n): ").lower()
    if play_again != "y":
        break

print("\nFinal Score -> You:", user_score, " Computer:", computer_score)

if user_score > computer_score:
    print("Congratulations, you won overall!")
elif user_score < computer_score:
    print("Computer won overall. Better luck next time!")
else:
    print("Overall, it's a tie!")

print("Thanks for playing!")
