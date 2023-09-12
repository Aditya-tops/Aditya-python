# Write a Python program to read first n lines of a file. 

n=int(input("Enternlines:- "))
f=open("myfile.txt","r")
for line in (f.readlines() [-n:]):
    print(line,end="")
f.close()