try:
    username = input("Your Username: ")
    if username == "Rambo":
        raise Exception
    else:
        print("Welcome", username)
except Exception:
    print("This username is busy")