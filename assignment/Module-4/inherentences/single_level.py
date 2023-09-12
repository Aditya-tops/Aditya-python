class Parent:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def  add(self):
        return self.n1+self.n2
class child(Parent):

    def sub(self):
        return self.n1-self.n2
    
obj=child(12,13)

print(obj.add())
print(obj.sub())