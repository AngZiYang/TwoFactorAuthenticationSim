# Two-Factor Authentication Simulator

This repository contains a Python-based simulation of a two-factor authentication (2FA) system. It demonstrates the generation and validation of one-time pins (OTPs) and user credential management in a secure, efficient manner.

## Overview

The system consists of two components:

1. **Device**: A script that generates time-based six-digit OTPs using a combination of the user's username, password, and a time seed.
2. **Connect**: A script for user registration and login, validating credentials and OTPs to ensure secure access.

The design highlights practical implementations of secure authentication mechanisms.

---

## Features

- **Dynamic OTP Generation**:
  - OTPs are generated based on SHA-256 hashing of the username, password, and time.
  - Pins are updated every 15 seconds and valid only within the corresponding time window.

- **User Management**:
  - Register new users with password confirmation and basic validation.
  - Store credentials in a plaintext file (`Passwords.txt`) for simplicity.

- **Credential Validation**:
  - Verify the username, password, and OTP for secure access during login.

- **How to run**:
  Device Program:
- Run the program with the command:
  python device.py [username] [password]

Connect Program:
- To register a new user, use:
  python connect.py [username] new
- To log in with a username, password, and pin:
  python connect.py [username] password [password] [pin]
