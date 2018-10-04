year = int(input())
print("Year: ",year)
century  = year//100+1

if year != 0 and year<=2004:
	print("Century: ",century)
else:
	print("Year is lower 0 or bigger 2005")
