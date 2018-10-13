str1 = "HI EVERYONE"
print(str1)
str2 = "!!! Welcome to the party."

def lower_str(func):
	def wrapper(*arg, **kwargs):
		return func(*arg, **kwargs)[0]+func(*arg, **kwargs)[1:].lower()
		
	return wrapper

def added(func1):
	def wrapper(*arg, **kwargs):
		return func1(*arg, **kwargs) + str2
		
	return wrapper

@added
@lower_str
def print_str(s):
	return s


print(print_str(str1))