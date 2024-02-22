from tkinter import *
from tkinter import messagebox
root = Tk()

def popup():
    messagebox.showinfo("This is my popup","helloworld")
    
btn = Button(root,text= "Popup",command=popup).pack()
root.mainloop()