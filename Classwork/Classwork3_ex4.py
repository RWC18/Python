list1 = [[5, 7, -7, 'abc'], [2, 4, True, 3], [4, 6, 7, 7], [2, 4, 1, True]] 
print("List1 = ",list1)
a = 0

for i in range(len(list1)):
	if a == 1:
		break
	for j in range(len(list1[0])):
		if list1[i][j] == 3:
			a=1
			break
		print("list1[i][j] = ",list1[i][j])