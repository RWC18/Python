list1 = [3, 6, True, True, -1, 'abc', (1, 2), [2, 3], 6]
print("List1 =",list1)
for i in range(len(list1)):
	if type(list1[i]) == tuple:
		break
	print("List1[i] =",list1[i])