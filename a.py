from tkinter import *
#ALL programs are here
root = Tk()
root.title("Login".center(200))# to change title name
root.iconbitmap("pic.ico")#to change icon; download ico file and save in file.
root.maxsize(width=800,height=800) # to change size to max 
root.minsize(width=250,height=400)# to minimize size of layout


#BUTTON
# redbutton = Button(root, text="LEFT", fg = "green")
# redbutton.pack(side = LEFT)
# greenbutton = Button(root, text="RIGHT", fg = "black")
# greenbutton.pack(side = RIGHT)
# bluebutton = Button(root, text="TOP", fg = "blue")
# bluebutton.pack(side = TOP)
# blackbutton = Button(root, text="BOTTOM", fg = "red")
# blackbutton.pack(side = BOTTOM)
# whitebutton = Button(root, text="Centre", fg = "yellow")
# whitebutton.pack(expand=True)


#LOGIN
# root.geometry('600x300')# max,min is better than this
# name = Label(root,text="Name").grid(row=0,column=0)
# a1 = Entry(root).grid(row=0,column=1)
# password = Label(root,text="Password").grid(row=1,column=0)
# a2 = Entry(root).grid(row=1,column=1)
# submit = Button(root, text = "Submit").grid(row = 4, column = 1)


# name = Label(root, text="Name").place(x = 30, y  = 50)
# address = Label(root, text = "Address").place(x = 30, y = 90)
# contact = Label(root, text = "Contact").place(x =30, y = 130)
# e1 = Entry(root).place(x = 80, y = 50)
# e2 = Entry(root).place(x = 80, y = 90)
# e3 = Entry(root).place(x = 95, y = 130)

name = Label(root, text="Name").place(x = 30, y  = 50)
email = Label(root, text = "Email").place(x = 30, y = 90)
password = Label(root, text = "Password").place(x =30, y = 130)
confirmPassword = Label(root, text = "ConfirmPassword").place(x =30, y = 170)
age = Label(root, text = "Age").place(x = 30,y = 210)

e1 = Entry(root).place(x = 140, y = 50)
e2 = Entry(root).place(x = 140, y = 90)
e3 = Entry(root).place(x = 140, y = 130)
e4 = Entry(root).place(x = 140, y = 170)
e5 = Entry(root).place(x = 140, y = 210)
# submit = Button(root, text = "Login").grid(row = 4, column = 1)
submit  = Button(root,text = "Login").place(x = 100, y  = 250)
root.configure(background ="#5a5a5a")

root.mainloop() # root is variable name