# creation of class

class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    
# creation of object

operation=Calculator(5,8)
result=operation.add()
print(result)
result=operation.sub()
print(result)
result=operation.mul()
print(result)
result=operation.div()
print(result)