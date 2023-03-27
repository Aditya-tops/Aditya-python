# from tkinter library we are importing all the functionality
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title("My Tkinter")
root.geometry("500x500")

def display_data():
    if e1.get() == "":
        msg.showinfo("Alert", "Name field is mandatory!!!")
    else:
        msg.showinfo("Your Name", e1.get())

# GUI element Label
name = Label(root, text="Enter name:", font=('Arial 12'))
name.place(x=50, y=50)

# GUI element box
e1 = Entry(root)
e1.place(x=150, y=50)

# GUI element button
btn1 = Button(root, text='SUBMIT', font=('Arial 12'), foreground="blue", background="teal", command=display_data)
btn1.place(x=100, y=100)

root.mainloop()
