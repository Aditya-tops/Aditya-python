# Write a python program to find the longest words. 
n=int(input("ENTER THE VALUE OF N "))

f=open("file.txt","r")
s=f.read()
lst=s.split()

'''for i in lst:
    if(len(i)>n):
        print(i)'''
print(max(lst,key=len))