import tkinter as tk

root = tk.Tk()
root.title("Entry operator")
root.geometry("300x300")

e = tk.Entry(root)
e.pack(pady=20)

def show():
    t = e.get()
    print("you have enter is",t)#edhi python window lo dispaly ayindhi
    l.config(text=f"you entered : {t}")#edhi gui lo padindhiii
    
b = tk.Button(root,text ="submit",command = show)
b.pack(pady=50)

l=tk.Label(root,text="ok lets check what is  inside")
l.pack(pady=50)

root.mainloop()

