# creation of class

class Student:

    def name(self,x):
        self.name=x
    def age(self,x):
        self.age=x
    def gender(self,x):
        self.gender=x
    def email(self,x):
        self.email=x
    def address(self,x):
        self.address=x


    def dispay(self):
        print("Name :- ",self.name)
        print("Age :- ",self.age)
        print("Gender :- ",self.gender)
        print("E-mail :- ",self.email)
        print("address :- ",self.address)

# creation of object

detail=Student()

detail.name(input("Enter your name :- "))
detail.age(int(input("Enter your age :- ")))
detail.gender(input("Enter your gender :- "))
detail.email(input("Enter your email :- "))
detail.address(input("Enter your address :- "))

detail.dispay()

print("")