class Mother:

    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2
    
class Father(Mother):

    def sub(self):
        return self.n1-self.n2

class child(Father):

    def mul(self):
        return self.n1*self.n2
    
obj=child(12,2)

print(obj.add())
print(obj.sub())
print(obj.mul())