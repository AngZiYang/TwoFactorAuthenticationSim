# Import modules
import time  # For handling time-related tasks
import hashlib  # For secure hash generation

# Generate a 6-digit pin based on username, password, and seed
def generate_pin(username, password, seed):
    """
    Creates a 6-digit pin using SHA-256 hashing.
    Combines username, password, and seed to generate a unique pin.
    """
    data = f"{username}{password}{seed}"  # Combine inputs
    hash_object = hashlib.sha256(data.encode())  # Generate hash
    pin = int(hash_object.hexdigest(), 16) % 1000000  # Get 6-digit pin
    return f"{pin:06d}"

# Continuously generate and display pins every 15 seconds
def run_device(username, password):
    """
    Continuously generates new pins every 15 seconds.
    Runs until stopped manually (Ctrl+C).
    """
    seed = time.time()  # Initial seed based on current time
    try:
        while True:
            pin = generate_pin(username, password, seed)
            print(f"Device: {pin}")
            time.sleep(15)  # Wait for 15 seconds
            seed += 15  # Update seed for the next pin
    except KeyboardInterrupt:
        print("Device stopped by user.")

# Entry point of the script
if __name__ == "__main__":
    import sys  # For handling command-line arguments
    username = sys.argv[1]  # Get username from command-line input
    password = sys.argv[2]  # Get password from command-line input
    run_device(username, password)  # Start the device


