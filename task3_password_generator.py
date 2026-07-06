# TASK 3 - PASSWORD GENERATOR (GUI VERSION)
# Generates a random password based on the length and
# character types chosen by the user, using Tkinter checkboxes.

import tkinter as tk
from tkinter import messagebox
import random
import string

# ---- Color palette ----
BG_COLOR = "#1b2631"        # dark navy background
PANEL_COLOR = "#273746"     # slightly lighter panel
TITLE_COLOR = "#f1c40f"     # yellow title
LABEL_COLOR = "white"
GEN_BUTTON_COLOR = "#16a085"   # teal
COPY_BUTTON_COLOR = "#2980b9"  # blue
TEXT_ON_BUTTON = "white"
RESULT_BG = "#f4f6f7"


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showinfo("Info", "No type selected. Using letters by default.")
        characters = string.ascii_letters

    password = ""
    for i in range(length):
        password += random.choice(characters)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


def copy_password():
    password = result_entry.get()
    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")


window = tk.Tk()
window.title("Password Generator")
window.geometry("380x360")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="🔐 Password Generator", font=("Arial", 17, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=15)

# Panel that holds the length + checkboxes, laid out with grid
panel = tk.Frame(window, bg=PANEL_COLOR, padx=15, pady=15)
panel.pack(padx=20, pady=5, fill="x")

tk.Label(panel, text="Length:", bg=PANEL_COLOR, fg=LABEL_COLOR, font=("Arial", 10)).grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(panel, width=8, font=("Arial", 11), justify="center")
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, padx=10)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(
    panel, text="Letters", variable=letters_var, bg=PANEL_COLOR, fg=LABEL_COLOR,
    selectcolor=PANEL_COLOR, font=("Arial", 9)
).grid(row=1, column=0, pady=8, sticky="w")

tk.Checkbutton(
    panel, text="Numbers", variable=numbers_var, bg=PANEL_COLOR, fg=LABEL_COLOR,
    selectcolor=PANEL_COLOR, font=("Arial", 9)
).grid(row=1, column=1, pady=8, sticky="w")

tk.Checkbutton(
    panel, text="Symbols", variable=symbols_var, bg=PANEL_COLOR, fg=LABEL_COLOR,
    selectcolor=PANEL_COLOR, font=("Arial", 9)
).grid(row=1, column=2, pady=8, sticky="w")

# Buttons side by side
action_frame = tk.Frame(window, bg=BG_COLOR)
action_frame.pack(pady=10)

tk.Button(
    action_frame, text="Generate", width=12, font=("Arial", 10, "bold"),
    bg=GEN_BUTTON_COLOR, fg=TEXT_ON_BUTTON, command=generate_password
).grid(row=0, column=0, padx=5)

tk.Button(
    action_frame, text="Copy", width=12, font=("Arial", 10, "bold"),
    bg=COPY_BUTTON_COLOR, fg=TEXT_ON_BUTTON, command=copy_password
).grid(row=0, column=1, padx=5)

result_entry = tk.Entry(
    window, width=32, justify="center", font=("Arial", 12, "bold"),
    bg=RESULT_BG
)
result_entry.pack(pady=15)

window.mainloop()
