import tkinter as tk

root = tk.Tk()
root.title("email verification")

def verification():
    user = u1.get()
    pwd = p1.get()
    if user == "admin" and pwd == "1234":
        l.config(text = "login success")
    else:
        l.config(text = "invalid id")
    

tk.Label(root,text = "username").grid(row = 0)
tk.Label(root,text= " password").grid(row = 1)

u1 = tk.Entry(root)#the place where u1,p1 are used in those same names are used
p1 = tk.Entry(root)

u1.grid(row = 0,column = 1)
p1.grid(row = 1,column = 1)

tk.Button(root,text = "submit",command = verification).grid(row = 2,column = 0)

l = tk.Label(root,text = "check id verification")
l.grid(row = 3,column = 2)

root.mainloop()
