# creation of class

class Sample:
    def __init__(self,x):
        self.num=x
    def display(self):
        print("Value :- ",self.num)

# creation of object

obj=Sample(300)
obj2=Sample(100)
obj.display()
obj2.display()