username = "Batman"
password = "I am Batman"
input_username = input("Enter a username: ")
input_password = input("Enter a password: ")

for i in range(1000000000000000000):
	if input_password == password and input_username == username:
		print("Welcome ;)")
		break
	else:
		print("Username or Password are wrong")
		input_username = input("Enter a username: ")
		input_password = input("Enter a password: ")
