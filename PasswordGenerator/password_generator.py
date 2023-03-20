import random
import string
import tkinter as tk
import pyperclip

def generate_password():
    length = length_var.get()
    if length < 8:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Password length must be at least 8.")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # Make the password more readable
    readable_password = ""
    for i in range(length):
        if i % 4 == 0 and i != 0:
            readable_password += "-"
        readable_password += password[i]
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, readable_password)
    
    # Create a copy button to copy the password to the clipboard
    copy_button = tk.Button(root, text="Copy Password", command=copy_password)
    copy_button.pack()

def copy_password():
    pyperclip.copy(password_entry.get())

root = tk.Tk()
root.title("Random Password Generator")

length_var = tk.IntVar(value=12)
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, variable=length_var)
length_scale.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root)
password_entry.pack()

root.mainloop()
