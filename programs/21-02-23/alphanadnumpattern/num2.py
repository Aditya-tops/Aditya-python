n = int(input("Enter number:"))
for i in range(n):
    for j in range(1,i+1):
        print(str(j%2), end=" ")
    print("")
