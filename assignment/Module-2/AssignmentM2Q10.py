''' WAP ewhich will return true if the two given integer 
    values are equal or their sum or difference is 5 '''

# 5 , 5 = true
# 2 + 3 = true
# 10 - 5 = true 

def test(x,y):
    if x==y or abs(x-y==5) or x+y == 5:
        return True
    else:
        return False
print(test(7,2))
print(test(2,2))
print(test(3,2))
print(test(27,53))
