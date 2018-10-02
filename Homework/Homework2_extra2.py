print("Input your number:")
input_num = int(input())
print("Number =", input_num)
i = input_num
fakt = 1
for q in range(1,(i+1)):
	fakt *=  i
	i -= 1
print(input_num,"factorial =",fakt)