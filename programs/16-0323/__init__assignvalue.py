# creation of class

class Sample:
    def __init__(self,name):
        self.namex=name
    def __str__(self):
        return "your name: "+self.namex
    
# creation of object

obj=Sample("ABC")
print(obj)
        