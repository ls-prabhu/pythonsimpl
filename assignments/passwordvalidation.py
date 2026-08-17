import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("650x500")
root.title("Password Validation")

password = tk.StringVar()

passentry = ttk.Entry(root, textvariable=password, justify="center", show="*",name="enter password")
passentry.pack(pady=10)

resultlbl = tk.StringVar()


def validation(userpass):
    errors = []
    allowedSpecialChar = ["@","%","#","!","^","&"]

    if len(userpass) < 8:
        errors.append("Password should contain at least 8 characters.")

    if not any(c.isupper() for c in userpass):
        errors.append("Password must contain at least one uppercase letter.")

    if not any(c.islower() for c in userpass):
        errors.append("Password must contain at least one lowercase letter.")

    if not any(c.isdigit() for c in userpass):
        errors.append("Password must contain at least one digit.")

    if not any(c in allowedSpecialChar for c in userpass):
        errors.append(f"Password must contain at least one special character: {', '.join(allowedSpecialChar)}")
    if errors:
        resultlbl.set("\n".join(errors))
    else:
        resultlbl.set("Your password was saved successfully!")
        password.set("")


ttk.Button(root, text="Submit",
           command=lambda: validation(password.get())).pack(pady=10)

ttk.Label(root, textvariable=resultlbl, foreground="red").pack()

root.mainloop()
