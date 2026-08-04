name = input("Enter your name: ")

if len(name) == 6:
    print("Access Denied: 6-character names are not allowed.")
else:
    print(f"Access Granted: Welcome, {name}!")