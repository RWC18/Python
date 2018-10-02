username = "Batman"
password = "I am Batman"


while True:
	input_username = input("Enter a username: ")
	input_password = input("Enter a password: ")
	if input_password == password and input_username == username:
		print("Welcome ;)")
		break
	else:
		print("Username or Password are wrong")
		
