class Parent:

    def func1(self):
        print("this function is in parent class")
    
class Child1(Parent):

    def func2(self):
        print("this function is in child1 class")

class Child2(Parent):

    def func3(self):
        print("this function is in child2 class")

obj1=Child1()
obj2=Child2()

obj1.func1()
obj1.func2()
print("")
obj2.func1()
obj2.func3()