# TASK 1 - TO-DO LIST APPLICATION (GUI VERSION)
# A simple to-do list app using Tkinter where the user can
# add, view, mark done, and delete tasks.
# Colors added to make the GUI look nicer.

import tkinter as tk
from tkinter import messagebox

tasks = []

# ---- Simple color palette (easy to change) ----
BG_COLOR = "#eaf6f6"        # light teal background
TITLE_COLOR = "#2c3e50"     # dark blue-grey text
BUTTON_COLOR = "#4CAF50"    # green
DELETE_COLOR = "#e74c3c"    # red
DONE_COLOR = "#3498db"      # blue
TEXT_ON_BUTTON = "white"


def refresh_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["done"] else "Not done"
        task_listbox.insert(tk.END, task["name"] + "  [" + status + "]")


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


# Main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("350x420")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="My To-Do List", font=("Arial", 16, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=10)

entry = tk.Entry(window, width=30, font=("Arial", 11))
entry.pack(pady=5)

add_button = tk.Button(
    window, text="Add Task", command=add_task,
    bg=BUTTON_COLOR, fg=TEXT_ON_BUTTON, font=("Arial", 10, "bold")
)
add_button.pack(pady=5)

task_listbox = tk.Listbox(
    window, width=40, height=12,
    bg="white", fg="black", selectbackground=DONE_COLOR
)
task_listbox.pack(pady=10)

button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=5)

done_button = tk.Button(
    button_frame, text="Mark as Done", command=mark_done,
    bg=DONE_COLOR, fg=TEXT_ON_BUTTON, font=("Arial", 10, "bold")
)
done_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame, text="Delete Task", command=delete_task,
    bg=DELETE_COLOR, fg=TEXT_ON_BUTTON, font=("Arial", 10, "bold")
)
delete_button.grid(row=0, column=1, padx=5)

window.mainloop()
