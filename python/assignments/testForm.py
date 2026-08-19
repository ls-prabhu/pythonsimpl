from tkinter import *
from tkinter import messagebox as m
q=[("What does CPU stand for?",["Central Processing Unit","Computer Personal Unit","Central Program Unit","Control Processing Unit"],"Central Processing Unit"),("Which language is used for web development?",["HTML","Python","C","All of these"],"All of these"),("What does RAM stand for?",["Random Access Memory","Read Access Memory","Run Access Memory","Random Application Memory"],"Random Access Memory"),("Which data type stores True or False?",["String","Boolean","Integer","Float"],"Boolean"),("Which symbol is used for assignment in Python?",["==","=","!=","=>"],"="),("Which keyword is used to define a function in Python?",["function","def","fun","define"],"def"),("Which one is an operating system?",["Python","Windows","Oracle","HTML"],"Windows"),("What does HTML stand for?",["Hyper Text Markup Language","High Text Machine Language","Hyper Tool Markup Language","Home Text Markup Language"],"Hyper Text Markup Language"),("Which symbol is used for comments in Python?",["//","#","/*","--"],"#"),("Which of these is a database?",["MySQL","HTML","CSS","Python"],"MySQL")]
r,i,s=Tk(),0,0
v,n=StringVar(),StringVar()
def g(a):
 for w in r.winfo_children():w.destroy()
 if a==len(q):Label(r,text=f"Done, {n.get()}!\nScore: {s}/{len(q)}",font=("Arial",16)).pack(pady=40);return Button(r,text="Exit",command=r.destroy).pack()
 Label(r,text=q[a][0],font=("Arial",14)).pack(pady=20);v.set(None)
 [Radiobutton(r,text=o,variable=v,value=o).pack(anchor="w")for o in q[a][1]]
 def h():
  global i,s
  if not v.get():return m.showwarning("Error","Select an answer")
  s+=v.get()==q[i][2];i+=1;g(i)
 Button(r,text="Next",command=h).pack(pady=20)
Label(r,text="Enter Name",font=("Arial",14)).pack(pady=20)
Entry(r,textvariable=n).pack()
Button(r,text="Start",command=lambda:g(0)if n.get()else m.showwarning("Error","Enter name")).pack(pady=20)
mainloop()