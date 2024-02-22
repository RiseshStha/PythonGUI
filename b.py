from tkinter import *
#Login page
root = Tk()

root.title('Login form')

root.minsize(700, 500)

root.configure(background='#b197fc')

e1 = Entry(root,bd=0).place(x=220, y=100)

email = Label(root, text='Email',padx=5,pady=3,bd=0,bg='#fff').place(x=220, y=130)

e2 = Entry(root,bd=0).place(x=220, y=170)
password = Label(root, text='Password',padx=5,pady=3,bd=0,bg='#fff').place(x=220, y=200)


login = Button(root,font='bold', text='Login',bg='#7950f2',bd=0,padx=13,width=15,fg='#fff').place(x=220, y=250)

root.mainloop()
