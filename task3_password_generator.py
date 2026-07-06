# TASK 3 - PASSWORD GENERATOR
# Generates a random password based on the length
# and character types chosen by the user.

import random
import string

print("----- PASSWORD GENERATOR -----")

length = int(input("Enter the desired password length: "))

use_letters = input("Include letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Build the pool of characters to choose from
characters = ""

if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("You didn't select any character type. Using letters by default.")
    characters = string.ascii_letters

password = ""
for i in range(length):
    password += random.choice(characters)

print("\nYour generated password is:")
print(password)
