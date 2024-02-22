from atexit import register
from tkinter import *
root = Tk()
# state =  Disable  is use to disable button 
#command = call function is like toast
def function():
    print("BUtton is Clicked")

def fun():
    myLabel = Label(root, text = "I Clicked Buttom", fg= "red",bg = "#000099",font=50)
    myLabel.pack()
# myButton = Button(root, text = "")
login = Button(root,text="Login", command = fun).place(x = 30, y = 90) # call function to use in command
registration = Button(root,text="Registration",state = DISABLED).place(x = 30, y = 120)
login = Button(root,text="ADD").place(x = 30, y = 150)
login = Button(root,text="Submit").place(x = 30, y = 180)
root.mainloop()