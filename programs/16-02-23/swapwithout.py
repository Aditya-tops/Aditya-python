# WAP that swap variable without using third variable

a = int(input("Enter the number A :- "))
b = int(input("Enter the number B :- "))

a=a+b
b=a-b
a=a-b

print("After Swapping A :-",a)
print("After Swapping B :-",b)
