from tkinter import *
root = Tk()
root.geometry("200x200")
def show():
    label.config(text = clicked.get())
    
options = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
optinon2 = ["Checking"]

clicked = StringVar()
clicked.set("monday")

drop = OptionMenu(root, clicked, *options,optinon2)
drop.pack()

button  = Button(root, text = "Click Me",command = show).pack()
label = Label(root, text = "")
label.pack()

root.mainloop()