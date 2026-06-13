import tkinter as tk
root = tk.Tk()
root.title("radio button operation")
root.geometry("300x300")

rv = tk.StringVar()
def show():
    t = rv.get()
    print("you have entered :",t)#it appeared on idle
    l.config(text=f"you entered : {t}")# it appear  on gui window
    
tk.Radiobutton(root,text="java",variable=rv,value = "1").pack()#value lo adhi pedithy adhi display avuthundhi
tk.Radiobutton(root,text="python",variable=rv,value = "python").pack()
tk.Radiobutton(root,text="c++",variable=rv,value = "c++").pack()

tk.Button(root,text="submit",command = show).pack()

l =tk.Label(root,text="hlo choose one")
l.pack(pady=50)

root.mainloop()
