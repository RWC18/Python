from rect import rectangle

def main_func():
	rec1 = rectangle(int(input("Enter lenght: " )), int(input("Enter width: " )))
	print("perimeter =",rec1.perimeter())
	print("area =",rec1.area())
if __name__ == "__main__":
	main_func()