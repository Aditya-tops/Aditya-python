class Bird:
    def __init__(self):
        self.__name = "duck"
        self.age = 2

    def display(self):
        print("Name of bird: ", self.__name)
        print("Age of bird: ", self.age)

obj = Bird()
obj.display()

print("Age outside the class:", obj.age)
# print("Name outside the class:", obj.__name)  # This will raise an AttributeError
