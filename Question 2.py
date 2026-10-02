import tkinter as tk

root = tk.Tk()
root.title("Special Midterm Exam in OOP ")
root.geometry("400x300")

def change_color():
    my_button.config(bg="yellow", fg="black")

my_button = tk.Button(root, text="Click To Change Color", command=change_color)
my_button.pack(pady=20)

root.mainloop()