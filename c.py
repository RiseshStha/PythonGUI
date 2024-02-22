from tkinter import*
root = Tk()
root.title("GUI")
maLabel = Label (root, text = "TKinter")
# e1 = Entry(root,bd=0).place(x=220, y=100)

email = Label(root, text='Tkinter',padx=5,pady=3,bd=0,bg='#fff')#.place(x=220, y=130)
email.pack(expand=True)
e2 = Entry(root,bd=0)#.place(x=220, y=170)
e2.pack(expand = True)
# password = Label(root, text='Password',padx=5,pady=3,bd=0,bg='#fff').place(x=220, y=200)


login = Button(root,font='bold', text='Login',bg='#7950f2',bd=0,padx=13,width=15,fg='#fff')#.place(x=220, y=250)
login.pack(expand=True)

root.mainloop()