#how to print factorial

n=int(input("Enter number :"))
factorial=1

for i in range(1,n+1):
    factorial=factorial*i
print(factorial)