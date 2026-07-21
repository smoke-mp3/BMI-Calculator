import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg="lightblue")

def calculate_bmi():
    try:
        weight = float(entry1.get())
        height = float(entry2.get())
        bmi = weight / (height ** 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    if bmi < 18.5:
       messagebox.showinfo("BMI Category", "You are underweight.")
    if bmi >= 18.5 and bmi < 24.9:
       messagebox.showinfo("BMI Category", "You have a normal weight.")
    if bmi >= 25 and bmi < 29.9:
       messagebox.showinfo("BMI Category", "You are overweight.")
    if bmi >= 30:
       messagebox.showinfo("BMI Category", "You are obese.")

def setup_gui():
    global label1, entry1, button1, label2, entry2, button2
    label1 = tk.Label(root, text="Enter your weight (kg):")
    entry1 = tk.Entry(root)
    label2 = tk.Label(root, text="Enter your height (m):")
    entry2 = tk.Entry(root)
    button1 = tk.Button(root, text="Calculate BMI", command=calculate_bmi)

    label1.pack(pady=(20,5))
    entry1.pack()
    label2.pack(pady=(10,5))
    entry2.pack()
    button1.pack(pady=15)

def get_font():
    font = tkFont.Font(family="Times new roman", size=16, weight="bold")
    return font
def background_color():
    root.configure(bg="lightblue")
    label1.configure(bg="lightblue")
    label2.configure(bg="lightblue")
    button1.configure(bg="lightblue")



if __name__ == '__main__':
    setup_gui()
    background_color()
    root.mainloop()