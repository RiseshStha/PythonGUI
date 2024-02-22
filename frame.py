from tkinter import*
my = Tk()
frame1 = LabelFrame(my,text = "This is my frame",padx=10,pady=10)
frame1.pack(padx=50,pady=50)
b = Button(frame1, text="Dont click here")
b2 = Button(frame1, text="...here")
b.grid(row=0,column=0)
b.grid(row=1,column=1)
my.mainloop()