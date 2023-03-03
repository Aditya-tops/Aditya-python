n=int(input("Enter the total Number of elements :- "))
l=[]
for i in range(n):
    element=input("Enter the elements :-")
    l.append(element)
print("My list :-",l)
non_duplicate_value=set(l)
print(non_duplicate_value)