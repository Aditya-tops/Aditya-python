# Write a Python program to read a file line by line and store it into a list

f=open("file.txt","r")
lines=f.readlines()

print(lines)

new_lines=[x.strip() for x in lines]
print(new_lines)