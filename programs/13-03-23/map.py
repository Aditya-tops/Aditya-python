# map(): to apply to operation of each iter element of the collection 
#it will return a map object 
#sytax : map(fun_name,collection)

def sqr(num):
    return num**2
l1=[1,2,3,4,5]
print(list(map(sqr,l1))) 