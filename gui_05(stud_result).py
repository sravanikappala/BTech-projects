import tkinter as tk

root = tk.Tk()
root.title("student marks cal")
def cal():
    m1 = int(e1.get()or 0)#sometimes not give output so use(or 0)
    m2 = int(e2.get()or 0)#this part is just like  to calculate code usinf correct formala and condition
    m3 = int(e3.get()or 0)
    total = m1+m2+m3
    avg = total/3
    l.config(text = f" total marks ={total},average = {avg:.2f}")

tk.Label(root,text ="maths").grid(row =0)
tk.Label(root,text ="science").grid(row =1)
tk.Label(root,text ="social").grid(row =2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)
e3.grid(row = 2,column = 1)

tk.Button(root,text = " submit", command = cal).grid(row = 3,column = 0)

l = tk.Label(root,text ="to check result")
l.grid(row = 4 ,column = 0)

root.mainloop()

