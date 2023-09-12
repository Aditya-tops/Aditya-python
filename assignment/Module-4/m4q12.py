# Write a Python program to copy the contents of a file to another file

f1=open("first.txt",mode="r",encoding="utf-8")
f2=open("second.txt",mode="w",encoding="utf-8")

data=(f1.readline())

for line in data:
    f2.write(line)


f1.close()
f2.close()