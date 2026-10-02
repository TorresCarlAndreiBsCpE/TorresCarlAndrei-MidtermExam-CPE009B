import tkinter as tk

root = tk.Tk()
root.title("Midterm in OOP")
root.geometry("500x350")


def display_name():
    user_input = entry_input.get()
    entry_output.config(state="normal")
    entry_output.delete(0, tk.END)
    entry_output.insert(0, user_input)
    entry_output.config(state="readonly")


namelabel_prompt = tk.Label(root, text="Enter your fullname:", fg="red")
namelabel_prompt.grid(row=0, column=0, padx=40, pady=20, sticky="e")

entry_input = tk.Entry(root, width=30)
entry_input.grid(row=0, column=1, padx=20, pady=20)

button_display = tk.Button(
    root, text="Click to display your Fullname", fg="red", command=display_name
)
button_display.grid(row=1, column=0, padx=40, pady=20, sticky="e")

# Set state="readonly" initially so the output entry cannot be manually edited
entry_output = tk.Entry(root, width=30, state="readonly")
entry_output.grid(row=1, column=1, padx=20, pady=20)

root.mainloop()