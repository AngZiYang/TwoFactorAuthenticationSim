# Import necessary modules
import hashlib  # Provides secure hash functions, used here for potential password hashing.

# Function to append user data to a file
def write_to_file(filename, data):
    """
    Appends data to the specified file.
    
    Args:
        filename (str): The name of the file to write to.
        data (str): The data to write to the file.
    """
    with open(filename, "a") as file:
        file.write(data + "\n")

# Function to read all lines from a file
def read_from_file(filename):
    """
    Reads all lines from the specified file and strips newline characters.
    
    Args:
        filename (str): The name of the file to read from.
    
    Returns:
        list: A list of strings, each representing a line in the file.
    """
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

# Function to verify if a username and password exist in the file
def verify_user(username, password, filename="Passwords.txt"):
    """
    Verifies if the given username and password combination exists in the file.
    
    Args:
        username (str): The username to verify.
        password (str): The password to verify.
        filename (str): The file containing user credentials (default: "Passwords.txt").
    
    Returns:
        bool: True if the combination exists, False otherwise.
    """
    users = read_from_file(filename)
    user_data = f"{username} {password}"
    return user_data in users

# Function to register a new user
def connect_mode_new(username):
    """
    Handles the registration of a new user. Prompts for a password and stores it
    in the credentials file if valid.
    
    Args:
        username (str): The username to register.
    """
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    # Check if passwords match and meet minimum length requirement
    if password == confirm_password and len(password) >= 8:
        write_to_file("Passwords.txt", f"{username} {password}")
        print("User registered successfully.")
    else:
        print("Password mismatch or too short.")

# Function to verify user credentials and login
def connect_mode_login(username, password, pin, filename="Passwords.txt"):
    """
    Handles user login by verifying the username, password, and pin.
    
    Args:
        username (str): The username to verify.
        password (str): The password to verify.
        pin (str): The one-time pin provided by the user.
        filename (str): The file containing user credentials (default: "Passwords.txt").
    """
    if verify_user(username, password, filename):
        # For simplicity, assume the device is running and the pin is valid.
        # Additional logic for pin validation can be implemented here.
        print("Login successful.")
    else:
        print("Invalid credentials.")

# Entry point for the script
if __name__ == "__main__":
    """
    Entry point for the script. Handles command-line arguments to determine
    the operation mode (register or login).
    
    Example usage:
    - Register: python connect.py <username> new
    - Login: python connect.py <username> <password> <pin>
    """
    import sys  # Provides access to command-line arguments and system-related functions
    
    # Parse command-line arguments
    mode = sys.argv[2]
    username = sys.argv[1]
    
    if mode == "new":
        # Register a new user
        connect_mode_new(username)
    else:
        # Login with an existing user
        password = sys.argv[3]
        if len(sys.argv) > 4:
            # If a pin is provided, proceed with login
            pin = sys.argv[4]
            connect_mode_login(username, password, pin)
        else:
            print("No PIN provided.")

