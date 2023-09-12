'''
How to Define a Class in Python? What Is Self? Give An Example Of
A Python Class 
'''

class mynumber:
	def __init__(self, value):
		self.value = value
	
	def print_value(self):
		print(self.value)

obj1 = mynumber(17)
obj1.print_value()
