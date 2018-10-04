def is_panidrome(text):
	reversed_string = text[::-1]
	if text == reversed_string:
		print(True)
	else:
		return print(False)

is_panidrome(str(input()))