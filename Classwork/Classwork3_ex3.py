for number in range(1,21):
	mod3 = number%3
	mod5 = number%5
	if mod3 == 0 and mod5 == 0:
		break
	print("Number =",number)