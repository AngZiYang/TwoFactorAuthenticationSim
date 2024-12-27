# Import modules
import hashlib  # For potential use in secure hashing

# Write data to a file
def write_to_file(filename, data):
    """
    Appends the given data to the specified file.
    """
    with open(filename, "a") as file:
        file.write(data + "\n")

# Read all lines from a file
def read_from_file(filename):
    """
    Reads and returns all lines from the specified file.
    """
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

# Check if a user exists in the file
def verify_user(username, password, filename="Passwords.txt"):
    """
    Verifies if the username and password combination exists in the file.
    """
    users = read_from_file(filename)
    user_data = f"{username} {password}"
    return user_data in users

# Register a new user
def connect_mode_new(username):
    """
    Registers a new user by prompting for a password and saving it to the file.
    """
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if password == confirm_password and len(password) >= 8:
        write_to_file("Passwords.txt", f"{username} {password}")
        print("User registered successfully.")
    else:
        print("Password mismatch or too short.")

# Login and verify credentials
def connect_mode_login(username, password, pin, filename="Passwords.txt"):
    """
    Logs in by verifying the username, password, and pin.
    """
    if verify_user(username, password, filename):
        print("Login successful.")
    else:
        print("Invalid credentials.")

# Entry point of the script
if __name__ == "__main__":
    import sys  # For handling command-line arguments
    mode = sys.argv[2]  # Get mode (new or login)
    username = sys.argv[1]  # Get username

    if mode == "new":
        connect_mode_new(username)  # Register a new user
    else:
        password = sys.argv[3]  # Get password
        if len(sys.argv) > 4:
            pin = sys.argv[4]  # Get pin
            connect_mode_login(username, password, pin)  # Login
        else:
            print("No PIN provided.")


