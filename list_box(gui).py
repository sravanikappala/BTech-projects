import tkinter as tk
root = tk.Tk()
root.title("list box operation")
root.geometry("300x300")

lb = tk.Listbox(root)
lb.insert(tk.END,"java")
lb.insert(tk.END,"python")
lb.insert(tk.END,"c")
lb.insert(tk.END,"c++")
lb.pack()

def show():
    selected = lb.curselection()
    if selected:
        value = lb.get(selected[0])
        l.config(text = f"selected is {value}")
    else:
        l.config(text = f"selected is invalid")

b = tk.Button(root,text ="submit" , command = show)
b.pack(pady = 20)

l = tk.Label(root,text = " ready ....??? ")
l.pack(pady = 30)

root.mainloop()
