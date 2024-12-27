import time
import hashlib

def generate_pin(username, password, seed):
    # Create a unique hash combining the username, password, and current time as a seed
    data = f"{username}{password}{seed}"
    hash_object = hashlib.sha256(data.encode())
    # Get a 6-digit pin from the hash
    pin = int(hash_object.hexdigest(), 16) % 1000000
    return f"{pin:06d}"

def run_device(username, password):
    seed = time.time()
    try:
        while True:
            pin = generate_pin(username, password, seed)
            print(f"Device: {pin}")
            time.sleep(15)  # Generate a new pin every 15 seconds
            seed += 15
    except KeyboardInterrupt:
        print("Device stopped by user.")

if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    run_device(username, password)
