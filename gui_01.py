##import tkinter as tk
##root = tk.Tk()
##root.title("label example")
##l1 = tk.Label(root,text = "welcome to vvitu",font = ("arial",16,"bold"),fg="blue")
##l1.pack(padx = 50,pady = 30)#if eedhi lykapothey label of vvitu display avadhuu
##root.mainloop()


##import tkinter as tk
##root = tk.Tk()
##root.title("button opeation")
##root.geometry("300x300")
##def show():
##    l.config(text="love u but right now missing u is more than love well ,\n i respect ur busy time but\n don't forget that i am there to spend time with u",fg = "red",bg = "black")
##
##b= tk.Button(root,text="click here",command = show)#ekkada command aneydhi function i indicate cheysthundhii anty aa button
##click ayyaka  em display avali aneydhi manam ready cheyali
##b.pack(padx =50,pady = 30)
##l = tk.Label(root,text = "hello, are u ready..?? to see my inner feeling ",font = ("arial",18), fg = "orange",bg = "purple")#label intial ga manaki kanipicheydhii
###so dhani ala visible cheyali aneydhi in our hands
##l.pack(pady = 50)
##root.mainloop()


import tkinter as tk
root = tk.Tk()
root.title("multiple checkbutton")
root.geometry("400x300")
c1 = tk.IntVar()
c2 = tk.IntVar()
c3  = tk.IntVar()
def show():
    print("python:",c1.get())
    print("java:",c2.get())
    print("c++:",c3.get())
    
tk.Checkbutton(root,text="python",variable = c1).grid(row = 0,column = 0)
tk.Checkbutton(root,text="java",variable = c2).grid(row = 1,column = 0)
tk.Checkbutton(root,text="c++",variable = c3).grid(row = 2,column = 0)
tk.Button(root,text = "submit",command = show).grid(row =3,column = 0)
root.mainloop()


##import tkinter as tk
##
##root = tk.Tk()
##root.title("multiple checkbutton")
##root.geometry("400x300")
##
##c1 = tk.IntVar()
##c2 = tk.IntVar()
##c3  = tk.IntVar()
##
##def show():
##    print("python:",c1.get())#if python ani click cheysthey c1.get(0 aneydhi 1 avuthundhi,
##    #so apudu after cliking it should display you entered python so that we use if and config operations
##    print("java:",c2.get())
##    print("c++:",c3.get())
##    if c1.get() == 1:
##        l.config(text=f"you entered is python")#here if use if iam selecting only one from above statements
##    elif c2.get() == 1:
##        l.config(text=f"you entered is java")
##    elif c3.get() == 1:        
##        l.config(text=f"you entered is c++")
##    else:
##        l.config(text="nothing")
##
##
##tk.Checkbutton(root,text="python",variable = c1).grid(row = 0,column = 0)
##tk.Checkbutton(root,text="java",variable = c2).grid(row = 1,column = 0)
##tk.Checkbutton(root,text="c++",variable = c3).grid(row = 2,column = 0)
##
##tk.Button(root,text = "submit",command = show).grid(row =3,column = 0)
##l = tk.Label(root,text ="ready to choose options")#.grid(row=3,column = 0)
##l.grid(row = 4,column = 0)
##
##root.mainloop()




























