# write a python program to count the number of characters (character frequency ) in astring

n=input("Enter the String: ").lower()
s={}
for i in n:
    if i in s:
        s[i]+=1 
    else:
        s[i]=1
print(s)
