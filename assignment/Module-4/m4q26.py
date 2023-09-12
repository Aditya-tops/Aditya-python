'''
Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?
'''
'''
- init method is the Python equivalent of the C++ constructor in an object-oriented approach
- constructor is a unique function that gets called automatically when an object is created of a class
'''

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