import hashlib

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

def read_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def verify_user(username, password, filename="Passwords.txt"):
    users = read_from_file(filename)
    user_data = f"{username} {password}"
    return user_data in users

def connect_mode_new(username):
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if password == confirm_password and len(password) >= 8:  # basic check for password length
        write_to_file("Passwords.txt", f"{username} {password}")
        print("User registered successfully.")
    else:
        print("Password mismatch or too short.")

def connect_mode_login(username, password, pin, filename="Passwords.txt"):
    if verify_user(username, password, filename):
        # Assume device is running and fetch the current valid pin
        print("Login successful.")
    else:
        print("Invalid credentials.")

if __name__ == "__main__":
    import sys
    mode = sys.argv[2]
    username = sys.argv[1]
    if mode == "new":
        connect_mode_new(username)
    else:
        password = sys.argv[3]
        if len(sys.argv) > 4:
            pin = sys.argv[4]
            connect_mode_login(username, password, pin)
        else:
            print("No PIN provided.")
