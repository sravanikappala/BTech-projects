##import tkinter as tk
##root = tk.Tk()
##root.title("text example")
##text_box = tk.Text(root,width =10,height = 5)
##text_box.pack(padx = 20,pady = 20)
##root.mainloop()



import tkinter as tk
root = tk.Tk()
root.title("canvas example")

canvas = tk.Canvas(root,width = 300,height = 200,bg = "white")
canvas.pack()

canvas.create_line(20,20,200,20,fill="red",width = 2)
canvas.create_rectangle(50,50,150,120,fill = "yellow")
canvas.create_oval(170,50,250,120,fill ="green")
canvas.create_text(150,170,text="canvas demo")


root.mainloop()
