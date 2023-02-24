city=input("Enter city:- ")
landmark=input("Enter landmark:- ")
state=input("Enter state:-")
temp=input("Enter temp:- ")
founder=input("Enter founder:- ")
humidity=input("Enter humidity:- ")
pin=input("Enter pin:- ")

var="""
{}, in {}, is the largest city in the {} state.

Weather: {},
Humidity: {}
Founded by: {}
Pincode: {}

""".format(city,landmark,state,temp,founder,humidity,pin)

print(var)
