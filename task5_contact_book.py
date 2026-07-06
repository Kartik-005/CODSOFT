# TASK 5 - CONTACT BOOK (GUI VERSION)
# A simple contact book using Tkinter where the user can
# add, view, search, update, and delete contacts.

import tkinter as tk
from tkinter import messagebox

contacts = []

# ---- Color palette ----
BG_COLOR = "#f4ecf7"        # light lavender background
PANEL_COLOR = "#d2b4de"     # soft purple panel
TITLE_COLOR = "#4a235a"     # deep purple text
ADD_COLOR = "#58d68d"
UPDATE_COLOR = "#5dade2"
DELETE_COLOR = "#ec7063"
SEARCH_COLOR = "#f5b041"
TEXT_ON_BUTTON = "black"


def refresh_list():
    contact_listbox.delete(0, tk.END)
    for c in contacts:
        contact_listbox.insert(tk.END, c["name"] + " - " + c["phone"])


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and phone number are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    clear_entries()
    refresh_list()
    messagebox.showinfo("Success", "Contact added successfully!")


def show_selected_contact(event):
    selected = contact_listbox.curselection()
    if not selected:
        return
    c = contacts[selected[0]]
    clear_entries()
    name_entry.insert(0, c["name"])
    phone_entry.insert(0, c["phone"])
    email_entry.insert(0, c["email"])
    address_entry.insert(0, c["address"])


def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return
    index = selected[0]
    contacts[index] = {
        "name": name_entry.get().strip(),
        "phone": phone_entry.get().strip(),
        "email": email_entry.get().strip(),
        "address": address_entry.get().strip()
    }
    refresh_list()
    messagebox.showinfo("Success", "Contact updated successfully!")


def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return
    index = selected[0]
    removed = contacts.pop(index)
    clear_entries()
    refresh_list()
    messagebox.showinfo("Deleted", "Deleted contact: " + removed["name"])


def search_contact():
    keyword = name_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    if keyword == "":
        refresh_list()
        return
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            contact_listbox.insert(tk.END, c["name"] + " - " + c["phone"])


window = tk.Tk()
window.title("Contact Book")
window.geometry("640x420")
window.configure(bg=BG_COLOR)

title_label = tk.Label(
    window, text="📇 Contact Book", font=("Arial", 17, "bold"),
    bg=BG_COLOR, fg=TITLE_COLOR
)
title_label.pack(pady=10)

# Main area split into two side-by-side sections: form on the left, list on the right
main_frame = tk.Frame(window, bg=BG_COLOR)
main_frame.pack(padx=15, pady=5, fill="both", expand=True)

# ---- Left side: form ----
left_panel = tk.Frame(main_frame, bg=PANEL_COLOR, padx=15, pady=15)
left_panel.grid(row=0, column=0, sticky="n", padx=(0, 10))

tk.Label(left_panel, text="Name:", bg=PANEL_COLOR, font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=4)
name_entry = tk.Entry(left_panel, width=22, font=("Arial", 10))
name_entry.grid(row=0, column=1, pady=4)

tk.Label(left_panel, text="Phone:", bg=PANEL_COLOR, font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=4)
phone_entry = tk.Entry(left_panel, width=22, font=("Arial", 10))
phone_entry.grid(row=1, column=1, pady=4)

tk.Label(left_panel, text="Email:", bg=PANEL_COLOR, font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=4)
email_entry = tk.Entry(left_panel, width=22, font=("Arial", 10))
email_entry.grid(row=2, column=1, pady=4)

tk.Label(left_panel, text="Address:", bg=PANEL_COLOR, font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=4)
address_entry = tk.Entry(left_panel, width=22, font=("Arial", 10))
address_entry.grid(row=3, column=1, pady=4)

# Buttons stacked vertically under the form instead of in a row
tk.Button(left_panel, text="Add", width=20, font=("Arial", 9, "bold"),
          bg=ADD_COLOR, command=add_contact).grid(row=4, column=0, columnspan=2, pady=(15, 3))
tk.Button(left_panel, text="Update", width=20, font=("Arial", 9, "bold"),
          bg=UPDATE_COLOR, command=update_contact).grid(row=5, column=0, columnspan=2, pady=3)
tk.Button(left_panel, text="Delete", width=20, font=("Arial", 9, "bold"),
          bg=DELETE_COLOR, command=delete_contact).grid(row=6, column=0, columnspan=2, pady=3)
tk.Button(left_panel, text="Search", width=20, font=("Arial", 9, "bold"),
          bg=SEARCH_COLOR, command=search_contact).grid(row=7, column=0, columnspan=2, pady=3)

# ---- Right side: contact list ----
right_panel = tk.Frame(main_frame, bg=BG_COLOR)
right_panel.grid(row=0, column=1, sticky="n")

tk.Label(right_panel, text="Saved Contacts", bg=BG_COLOR, fg=TITLE_COLOR,
         font=("Arial", 11, "bold")).pack(anchor="w")

contact_listbox = tk.Listbox(right_panel, width=40, height=16, bg="white", selectbackground=UPDATE_COLOR)
contact_listbox.pack(pady=5)
contact_listbox.bind("<<ListboxSelect>>", show_selected_contact)

tk.Label(
    right_panel, text="Tip: type in Name/Phone on the left and click Search.",
    font=("Arial", 8), bg=BG_COLOR
).pack(anchor="w")

window.mainloop()
