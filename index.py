import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        previous_year = float(previous_year_entry.get())
        this_year = float(this_year_entry.get())
        result = this_year - previous_year
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def print_receipt():
    # Print receipt logic goes here
    pass

# Create main window
root = tk.Tk()
root.title("Water Usage Calculator")

# Add input fields
previous_year_label = tk.Label(root, text="Previous Year:")
previous_year_label.grid(row=0, column=0)
previous_year_entry = tk.Entry(root)
previous_year_entry.grid(row=0, column=1)

this_year_label = tk.Label(root, text="This Year:")
this_year_label.grid(row=1, column=0)
this_year_entry = tk.Entry(root)
this_year_entry.grid(row=1, column=1)

# Add buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

print_button = tk.Button(root, text="Print Receipt", command=print_receipt)
print_button.grid(row=3, column=0, columnspan=2, pady=10)

# Display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the application
root.mainloop()
