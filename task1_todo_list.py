# TASK 1 - TO-DO LIST APPLICATION (GUI VERSION) - IMPROVED
# A simple to-do list app using Tkinter where the user can
# add, view, mark done, and delete tasks.
# This version has a nicer, more polished layout.

import tkinter as tk
from tkinter import messagebox

tasks = []

# ---- Color palette (easy to change) ----
BG_COLOR = "#f5f6fa"        # light grey-white background
HEADER_COLOR = "#6c5ce7"    # purple header bar
HEADER_TEXT = "white"
CARD_COLOR = "white"
ENTRY_BORDER = "#dcdde1"
ADD_COLOR = "#00b894"       # green
DONE_COLOR = "#0984e3"      # blue
DELETE_COLOR = "#d63031"    # red
TEXT_ON_BUTTON = "white"
COUNT_COLOR = "#636e72"


def refresh_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            display_text = "✔  " + task["name"] + "   (done)"
        else:
            display_text = "•  " + task["name"]
        task_listbox.insert(tk.END, display_text)

    # Color completed tasks differently in the list
    for i, task in enumerate(tasks):
        if task["done"]:
            task_listbox.itemconfig(i, fg="#95a5a6")
        else:
            task_listbox.itemconfig(i, fg="#2d3436")

    count_label.config(text=str(len(tasks)) + " task(s) total")


def add_task():
    task_name = entry.get().strip()
    if task_name == "":
        messagebox.showwarning("Warning", "Please enter a task name.")
        return
    tasks.append({"name": task_name, "done": False})
    entry.delete(0, tk.END)
    refresh_list()


def mark_done():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task first.")
        return
    index = selected[0]
    tasks[index]["done"] = True
    refresh_list()


def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task first.")
        return
    index = selected[0]
    removed = tasks.pop(index)
    refresh_list()
    messagebox.showinfo("Deleted", "Deleted task: " + removed["name"])


# Let pressing Enter in the entry box also add the task
def on_enter_key(event):
    add_task()


# ---- Main window ----
window = tk.Tk()
window.title("To-Do List")
window.geometry("380x480")
window.configure(bg=BG_COLOR)

# ---- Header bar ----
header = tk.Frame(window, bg=HEADER_COLOR, pady=18)
header.pack(fill="x")

title_label = tk.Label(
    header, text="📝 My To-Do List", font=("Arial", 18, "bold"),
    bg=HEADER_COLOR, fg=HEADER_TEXT
)
title_label.pack()

# ---- Input card ----
input_card = tk.Frame(window, bg=CARD_COLOR, padx=15, pady=15)
input_card.pack(padx=20, pady=15, fill="x")

entry = tk.Entry(
    input_card, width=24, font=("Arial", 11),
    relief="solid", bd=1, highlightbackground=ENTRY_BORDER
)
entry.grid(row=0, column=0, padx=(0, 8), ipady=4)
entry.bind("<Return>", on_enter_key)

add_button = tk.Button(
    input_card, text="+ Add", font=("Arial", 10, "bold"),
    bg=ADD_COLOR, fg=TEXT_ON_BUTTON, relief="flat", padx=10,
    command=add_task
)
add_button.grid(row=0, column=1)

# ---- Task count label ----
count_label = tk.Label(window, text="0 task(s) total", font=("Arial", 9), bg=BG_COLOR, fg=COUNT_COLOR)
count_label.pack(anchor="w", padx=25)

# ---- Task list card ----
list_card = tk.Frame(window, bg=CARD_COLOR, padx=10, pady=10)
list_card.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(list_card)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(
    list_card, width=40, height=12, font=("Arial", 11),
    bg="white", relief="flat", selectbackground="#dfe6e9",
    yscrollcommand=scrollbar.set, activestyle="none"
)
task_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

# ---- Action buttons ----
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=15)

done_button = tk.Button(
    button_frame, text="✔ Mark as Done", font=("Arial", 10, "bold"),
    bg=DONE_COLOR, fg=TEXT_ON_BUTTON, relief="flat", padx=10, pady=5,
    command=mark_done
)
done_button.grid(row=0, column=0, padx=8)

delete_button = tk.Button(
    button_frame, text="🗑 Delete", font=("Arial", 10, "bold"),
    bg=DELETE_COLOR, fg=TEXT_ON_BUTTON, relief="flat", padx=10, pady=5,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=8)

window.mainloop()
