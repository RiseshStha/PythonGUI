from tkinter import*
root = Tk()
root.title("GUI")
root.maxsize(width=600,height = 300)
root.minsize(width=600,height=300)
def add():
    x = var.get()
    print(x)
    myLabel1.config(text = x,bg= "green")
    
myLabel = Label(root, text = "UserName",fg= "red",bg= "yellow")
myLabel.place(x=30,y=10)

myLabel1 = Label(root, text= "Nothing",fg="red",bg="yellow")
myLabel1.place(x=40,y=120)
var = StringVar()
ent = Entry(root, text = "Submit",fg="black",textvariable=var)
ent.place(x=80,y =10)

btn = Button(root, text="Submit",bg="green",fg="white",command=add)
btn.place(x=20, y =80)

root.mainloop()
