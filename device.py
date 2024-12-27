# Import necessary modules
import time  # Provides time-related functions, such as time delays and getting the current time.
import hashlib  # Used for hashing data securely using algorithms like SHA-256.

# Function to generate a 6-digit pin based on the username, password, and seed value
def generate_pin(username, password, seed):
    """
    Generate a unique 6-digit pin.
    
    The pin is derived by hashing a combination of the username, password, 
    and a time-based seed using SHA-256. The result is then truncated to 
    six digits for use as a one-time pin (OTP).

    Args:
        username (str): The username of the user.
        password (str): The user's password.
        seed (float): A time-based seed value.

    Returns:
        str: A 6-digit pin as a string.
    """
    # Create a string combining the username, password, and seed
    data = f"{username}{password}{seed}"
    
    # Hash the combined string using SHA-256
    hash_object = hashlib.sha256(data.encode())
    
    # Convert the hash to a 6-digit number
    pin = int(hash_object.hexdigest(), 16) % 1000000
    
    # Ensure the pin is zero-padded to 6 digits
    return f"{pin:06d}"

# Function to continuously generate and display pins
def run_device(username, password):
    """
    Continuously generate and display a new pin every 15 seconds.
    
    The function calculates a new pin using the `generate_pin` function
    and updates the seed value every 15 seconds. The process runs indefinitely
    until manually stopped by the user (Ctrl+C).

    Args:
        username (str): The username of the user.
        password (str): The user's password.
    """
    # Initialize the seed with the current time
    seed = time.time()
    
    try:
        # Infinite loop to generate and display pins
        while True:
            # Generate a pin using the current seed
            pin = generate_pin(username, password, seed)
            
            # Display the pin
            print(f"Device: {pin}")
            
            # Wait for 15 seconds before generating the next pin
            time.sleep(15)
            
            # Increment the seed by 15 seconds for the next pin
            seed += 15
    except KeyboardInterrupt:
        # Handle user interrupt (Ctrl+C)
        print("Device stopped by user.")

# Entry point for the script
if __name__ == "__main__":
    """
    Entry point for the script. The script expects two command-line arguments:
    1. The username
    2. The password

    Example usage:
    python device.py <username> <password>
    """
    import sys  # Provides access to command-line arguments and system functions
    
    # Get the username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    
    # Run the device functionality
    run_device(username, password)

