from tkinter import *

# Create main window
root = Tk()
root.title("Basic Calculator")
root.geometry("500x400")
root.resizable(True, True)

# Input field
entry = Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to add numbers/operators
def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

# Function to clear display
def clear():
    entry.delete(0, END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = Button(root, text=text, width=6, height=2,
                     font=("Arial", 16), bg="lightgreen",
                     command=calculate)
    else:
        btn = Button(root, text=text, width=6, height=2,
                     font=("Arial", 16),
                     command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = Button(root, text="C", width=28, height=2,
                   font=("Arial", 14), bg="tomato",
                   command=clear)

clear_btn.grid(row=5, column=0, columnspan=4, pady=10)

# Run app
root.mainloop()