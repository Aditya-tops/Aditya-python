class Bird:
    def __init__(self):
        self.__name = "Duck"
        self.age = 2

    def display(self):
        print("Name of bird: ", self.__name)
        print("Age of bird: ", self.age)

obj = Bird()

print("Age outside the class: ", obj.age)
# Accessing the private instance variable using its mangled name
print("Name outside the class: ", obj._Bird__name)
