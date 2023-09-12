class School:

    def fun1(self):
        print("i m the school class")

class Teacher1(School):

    def fun2(self):
        print("i m a teacher 1 ")

class Teacher2(School):

    def fun3(self):
        print("i m a teacher 2 ")

class student(Teacher1,Teacher2):

    def fun4(self):
        print("i m student ")


obj=student()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()