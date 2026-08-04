name = input("Enter your name: ")

if len(name) >= 6:
    print("Access Denied: Names with 6 or more characters are not allowed.")
else:
    print(f"Access Granted: Welcome, {name}!")