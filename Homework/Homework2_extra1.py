import re
while True:
	password = input("Enter a password: ")
	if len(password) < 8:
		print("Your password hasn't 8 letters")
	elif not re.search(r"[A-Z]", password):
		print("Your password hasn't any capital letters")
	elif not re.search(r"[0-9]", password):
		print("Your password hasn't any numbers")
	else:
		print("Your password is true")
		break
