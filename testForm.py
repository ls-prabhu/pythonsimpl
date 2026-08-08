import tkinter as tk
from tkinter import messagebox

q = [
    (
        "What does CPU stand for?",
        [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Unit",
            "Control Processing Unit",
        ],
        "Central Processing Unit",
    ),
    (
        "Which language is used for web development?",
        ["HTML", "Python", "C", "All of these"],
        "All of these",
    ),
    (
        "What does RAM stand for?",
        [
            "Random Access Memory",
            "Read Access Memory",
            "Run Access Memory",
            "Random Application Memory",
        ],
        "Random Access Memory",
    ),
    (
        "Which data type stores True or False?",
        ["String", "Boolean", "Integer", "Float"],
        "Boolean",
    ),
    (
        "Which symbol is used for assignment in Python?",
        ["==", "=", "!=", "=>"],
        "=",
    ),
    (
        "Which keyword is used to define a function in Python?",
        ["function", "def", "fun", "define"],
        "def",
    ),
    (
        "Which one is an operating system?",
        ["Python", "Windows", "Oracle", "HTML"],
        "Windows",
    ),
    (
        "What does HTML stand for?",
        [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Tool Markup Language",
            "Home Text Markup Language",
        ],
        "Hyper Text Markup Language",
    ),
    ("Which symbol is used for comments in Python?", ["//", "#", "/*", "--"], "#"),
    ("Which of these is a database?", ["MySQL", "HTML", "CSS", "Python"], "MySQL"),
]

root, i, score = tk.Tk(), 0, 0
root.title("Quiz")
v, name = tk.StringVar(), tk.StringVar()


def show():
  global i, score
  for w in root.winfo_children():
    w.destroy()

  if i == len(q):
    tk.Label(
        root,
        text=f"Done, {name.get()}!\nScore: {score}/{len(q)}",
        font=("Arial", 16),
    ).pack(pady=40)
    return tk.Button(root, text="Exit", command=root.destroy).pack()

  tk.Label(root, text=q[i][0], font=("Arial", 14)).pack(pady=20)
  v.set(None)  # Clears any previous selection so none are selected initially
  for opt in q[i][1]:
    tk.Radiobutton(root, text=opt, variable=v, value=opt).pack(anchor="w")

  def nxt():
    global i, score
    if not v.get():
      return messagebox.showwarning("Error", "Select an answer")
    if v.get() == q[i][2]:
      score += 1
    i += 1
    show()

  tk.Button(root, text="Next", command=nxt).pack(pady=20)


tk.Label(root, text="Enter Name", font=("Arial", 14)).pack(pady=20)
tk.Entry(root, textvariable=name).pack()
tk.Button(
    root,
    text="Start",
    command=lambda: show()
    if name.get()
    else messagebox.showwarning("Error", "Enter name"),
).pack(pady=20)

root.mainloop()
