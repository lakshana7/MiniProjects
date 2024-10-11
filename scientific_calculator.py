import tkinter as tk
import math
from fractions import Fraction

def on_click(button_text):
    current_text = entry_var.get()
    
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    elif button_text == "←":
        entry_var.set(current_text[:-1])
    elif button_text == "x^2":
        entry_var.set(f"({current_text})**2")
    elif button_text == "√x":
        entry_var.set(f"math.sqrt({current_text})")
    elif button_text == "exp":
        entry_var.set(f"math.exp({current_text})")
    elif button_text == "log":
        entry_var.set(f"math.log({current_text})")
    elif button_text == "to frac":  # Convert to fraction
        try:
            decimal_value = float(current_text)
            fraction_value = Fraction(decimal_value).limit_denominator()
            entry_var.set(str(fraction_value))
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="black")  # Set background color to black

# Entry widget to display the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 14), justify="right", bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('←', 5, 1),
    ('x^2', 5, 2), ('√x', 5, 3),
    ('exp', 6, 0), ('log', 6, 1),
    ('to frac', 6, 2),  # Convert to fraction
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: on_click(t), bg="blue", fg="white")
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

# Run the Tkinter event loop
root.mainloop()
