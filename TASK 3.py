import random
from tkinter import *
from tkinter.ttk import *


def generate_password():
    entry.delete(0, END)

    length = var1.get()

    if not length:  # Default length if combobox value is empty
        length = 8

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789 !@#$%^&*()"

    password = ""

    if var.get() == 1:  # Low complexity
        characters = lower
    elif var.get() == 0:  # Medium complexity
        characters = upper
    elif var.get() == 3:  # Strong complexity
        characters = lower + upper + digits
    else:
        print("Please choose an option")
        return

    for _ in range(length):
        password += random.choice(characters)

    return password


def generate():
    password1 = generate_password()
    entry.insert(0, password1)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


def clear_entry():
    entry.delete(0, END)


def exit_app():
    root.quit()


root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")

# Label for password entry
Random_password = Label(root, text="Password")
Random_password.grid(row=0, column=0, padx=10, pady=10)

# Entry widget to show password
entry = Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

# Length label
c_label = Label(root, text="Length")
c_label.grid(row=1, column=0, padx=10, pady=10)

# Copy, Generate, Clear, and Exit buttons
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2, padx=10, pady=10)

generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3, padx=10, pady=10)

clear_button = Button(root, text="Clear", command=clear_entry)
clear_button.grid(row=1, column=2, padx=10, pady=10)

exit_button = Button(root, text="Exit", command=exit_app)
exit_button.grid(row=1, column=3, padx=10, pady=10)

# Radio buttons for complexity
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=1, padx=10, pady=10, sticky='W')

radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=2, padx=10, pady=10, sticky='W')

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=3, padx=10, pady=10, sticky='W')

# Combobox for length selection
combo = Combobox(root, textvariable=var1, state="readonly")
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>', lambda event: var1.set(combo.get()))
combo.grid(column=1, row=1, padx=10, pady=10)

root.mainloop()
