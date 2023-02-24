a = int(input("Enter number: "))
n = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(n, end=" ")
        n += 1
    print()