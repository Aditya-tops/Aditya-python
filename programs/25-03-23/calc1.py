from tkinter import *

root = Tk()
root.title("My Calculator")
root.geometry("420x300+100+200")

class Mywindow:
    def __init__(self,master):
        
        # lable and place

        self.lbl1 = Label(master, text='First number', font=('arial', 15))
        self.lbl1.place(x=10, y=50)

        self.lbl2 = Label(master, text='Second number', font=('arial', 15))
        self.lbl2.place(x=10, y=100)

        self.lbl3 = Label(master, text='Result', font=('arial', 15))
        self.lbl3.place(x=10, y=200)


        # Entry box

        self.t1 = Entry(bd=3, font=("arial", 12))
        self.t1.place(x=200, y=50)

        self.t2 = Entry(bd=3, font=("arial", 12))
        self.t2.place(x=200, y=100)

        self.t3 = Entry(bd=3, font=("arial", 12))
        self.t3.place(x=200, y=200)
        
        # Button

        self.b1 = Button(master, width=10, text='Add', command=self.add, font=('arial', 10), bg=('blue'))
        self.b1.place(x=10, y=150)
        self.b2 = Button(master, width=10, text='Sub', command=self.sub, font=('arial', 10), bg=('blue'))
        self.b2.place(x=110, y=150)
        self.b3 = Button(master, width=10, text='Mult', command=self.multi, font=('arial', 10), bg=('blue'))
        self.b3.place(x=210, y=150)
        self.b4 = Button(master, width=10, text='Div', command=self.div, font=('arial', 10), bg=('blue'))
        self.b4.place(x=310, y=150)


    def add(self):

        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    # operation 
    
    def sub(self):

        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))
 
    def multi(self):

        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self):

        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))


Operation = Mywindow(root)
root.mainloop()
