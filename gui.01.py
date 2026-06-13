import tkinter as tk
root = tk.Tk()
root.title("sample GUI with labels,entry and button")
root.geometry('400x300')

l1 = tk.Label(root,text="name")
l2 = tk.Label(root,text="age")

l1.grid(row = 0,column = 0)
l2.grid(row = 1,column = 0)#untill here it shows name and age not have scope to enter output

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)#untill here shows name and age asa label and can show empty box to enter info

def show():
    print("name:",e1.get())#e1.get() shows what name the user entered
    print("age:",e2.get())
    
b = tk.Button(root,text="submit",command=show)
b.grid(row=2,column=1)#display the button option in order to cliking the button only it will display

root.mainloop()
