# Write a Python program to count the number of lines in a text file. 

file=open('data.txt')
count=0
content=file.read()
conList=content.split("\n")
for i in conList;
    if i:
        count+=1
print("Number of lines in file are:",count)