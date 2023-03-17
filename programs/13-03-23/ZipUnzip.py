l1=[1,2,3,4]
l2=["one","two","three"]

# zipping of two lists
z1=zip(l1,l2)

# unzipping of lists
a,b=zip(*z1)  # unpack operator 

print(a)
print(b)