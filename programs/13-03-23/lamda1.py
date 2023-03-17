# lamda function as returity from another function

def myfunc(n1):
    return lambda p:p+n1
# to call myfunc
var=myfunc(2) #lamda p:p+n1

# to call returning lambda func

print(var(2))