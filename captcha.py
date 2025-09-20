import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def check_captcha():
    if entry.get() == captcha_text.get():
        messagebox.showinfo("Success", "CAPTCHA verified successfully!")
        root.quit()
    else:
        messagebox.showerror("Error", "Wrong CAPTCHA! Try again.")
        new_captcha()

def new_captcha():
    captcha_text.set(generate_captcha())
    captcha_label.config(text=captcha_text.get())
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple CAPTCHA")
root.geometry("300x200")
root.configure(bg="lightblue")

captcha_text = tk.StringVar()
captcha_text.set(generate_captcha())

tk.Label(root, text="Enter CAPTCHA:", font=("Arial", 12), bg="lightblue").pack(pady=10)
captcha_label = tk.Label(root, text=captcha_text.get(), font=("Arial", 20, "bold"), bg="white")
captcha_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Verify", command=check_captcha).pack(pady=5)
tk.Button(root, text="Refresh", command=new_captcha).pack(pady=5)

root.mainloop()