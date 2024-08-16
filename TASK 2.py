import tkinter
from tkinter import *
import math

root = Tk()
root.title("Advanced Calculator")
root.geometry("570x700+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

# Safe evaluation function using eval
def safe_eval(expr):
    try:
        # Replace the square root symbol with the actual sqrt function
        expr = expr.replace('√', 'math.sqrt')
        return str(eval(expr, {"__builtins__": None, "math": math}, {}))
    except ZeroDivisionError:
        return "Error: Division by Zero"
    except Exception as e:
        return "Error"

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        result = safe_eval(equation)
        equation = result
    label_result.config(text=result)

# Keyboard input handling
def on_key_press(event):
    key = event.char
    if key in '0123456789ABCDEF+-*/.^√':
        show(key)
    elif key == '\r':  # Enter key for calculate
        calculate()
    elif key == '\x08':  # Backspace key for clear
        clear()

label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Adding more operator buttons
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#FF6347", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="A", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("A")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="B", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("B")).place(x=10, y=200)
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("7")).place(x=150, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("8")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("C")).place(x=10, y=300)
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("4")).place(x=150, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("5")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="D", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("D")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="E", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("E")).place(x=430, y=400)

Button(root, text="F", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#555", command=lambda: show("F")).place(x=10, y=500)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show("0")).place(x=150, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#333", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#FFA500", command=lambda: calculate()).place(x=430, y=400)

# New operator buttons
Button(root, text="^", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("**")).place(x=10, y=600)
Button(root, text="//", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("//")).place(x=150, y=600)
Button(root, text="mod", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("%")).place(x=290, y=600)
Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#1E90FF", command=lambda: show("√(")).place(x=430, y=600)

# Bind keys to the root window
root.bind("<Key>", on_key_press)

root.mainloop()
