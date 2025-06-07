import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def prod(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CASIO Calculator")
        
        # Create input fields
        self.num1_label = tk.Label(master, text="Enter first number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(master)
        self.num1_entry.pack()
        
        self.num2_label = tk.Label(master, text="Enter second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(master)
        self.num2_entry.pack()
        
        # Create buttons for operations
        self.add_button = tk.Button(master, text="Add", command=self.add_numbers)
        self.add_button.pack()
        
        self.sub_button = tk.Button(master, text="Subtract", command=self.sub_numbers)
        self.sub_button.pack()
        
        self.prod_button = tk.Button(master, text="Multiply", command=self.prod_numbers)
        self.prod_button.pack()
        
        self.div_button = tk.Button(master, text="Divide", command=self.div_numbers)
        self.div_button.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def add_numbers(self):
        self.calculate(add)

    def sub_numbers(self):
        self.calculate(sub)

    def prod_numbers(self):
        self.calculate(prod)

    def div_numbers(self):
        self.calculate(div)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = operation(num1, num2)
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()