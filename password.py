import tkinter as tk
import random
import string

def generate_password():
    try:
      length=int(length_entry.get())
    except ValueError:
         result_var.set("Invalid input.Enter a number.")
         return
    
    if length<1:
        result_var.set("Password length must be at least 1")
        return
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

root=tk.Tk()
root.title("Password Generator")

length_label=tk.Label(root,text=" Enter Password Length:")
length_label.pack(pady=10)

length_entry=tk.Entry(root)
length_entry.pack(pady=10)

generate_button=tk.Button(root,text="Generate Password",command=generate_password)
generate_button.pack(pady=10)

result_var=tk.StringVar()
result_label=tk.Label(root,textvariable=result_var,font=('Arial',12,'bold'))
result_label.pack(pady=10)

copy_button=tk.Button(root,text="Copy to Clipboard",command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()