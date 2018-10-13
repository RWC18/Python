list1 = ['Anna', 'Edgar']
print("List1 =",list1)
list2 = ['Eliza', 'Ani', 'Vardan']
print("List2 =",list2)

def decorator(func):
	def wrapper(*arg, **kwargs):
		print("List1 befor append:",list1)
		func(*arg,**kwargs)
		print("List1 after append:",list1)
	return(wrapper)

@decorator
def add_values(list2):
	for i in range(len(list2)):
		list1.append(list2[i])

add_values(list2)
