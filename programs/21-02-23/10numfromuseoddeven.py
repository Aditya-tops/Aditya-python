""" WAP that take input 10 numbers form user and identify even or odd.
        *Add all even numbers.
        *Add all odd numbers.
        *count odd and even. """

k=0
j=0
temp=0
odd=0

l=int(input("Enter how many number you want to compare:"))
for i in range(0,l):
    a=int(input("Enter Number:"))
    if a%2==0:
        print(a,"is even number.")
        k=k+1
        temp=temp+a
    else:
        j=j+1
        odd=odd+a
        print(a,"is odd number.")
print("Total number of even number:",k)
print("Total number of odd number:",j)
print("Addition of even number:",temp)
print("Addition of even number:",odd)
