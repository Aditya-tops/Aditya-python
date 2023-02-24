n = int(input("Enter number:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()