l1 = [0,"a",2]
for i in range(len(l1)):
	num = l1[i]
	try:
		num = 1/num
		print(num)
	except Exception as e:
	    print("List item is 'Str' or '0'")