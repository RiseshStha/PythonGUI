from tkinter import*
my = Tk()
e = Entry(my, width = 50,bg = "green",fg = "white",borderwidth =5, font = 20)
e.pack()
# my.bind()

def getText():
    myLabel = Label(my, text = "Hello "+ e.get())
    myLabel.pack()
    e.delete(0, END)
    
    
button = Button(my, text = "Click me",padx = 10, pady =10, command = getText)
button.pack()

my.mainloop()