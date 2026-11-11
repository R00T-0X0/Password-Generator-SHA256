# Password Generator & SHA-256 Hasher

This is a simple Python project that I built to practice some basic cybersecurity concepts.

The program generates random passwords using Python's `secrets` module and calculates the SHA-256 hash of the generated password.

## What does it do?

- Generates passwords with a custom length.
- Uses uppercase and lowercase letters.
- Includes numbers and special characters.
- Uses `secrets` to generate passwords securely.
- Calculates the SHA-256 hash using `hashlib`.
- Displays the hash in hexadecimal format.

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

Clone the repository:

```bash
git clone https://github.com/R00T-0X0/Password-Generator-SHA256.git
```

Move into the project directory:

```bash
cd Password-Generator-SHA256
```

Run the script:

```bash
python password_generator_hasher.py
```

Enter the password length when requested.

## Example

```text
Enter password length: 16

=============================================
       PASSWORD GENERATOR & SHA-256
=============================================

Generated Password : YourGeneratedPassword
SHA-256 Hash        : YourSHA256Hash

=============================================
```

The password and hash will be different each time the program runs.

## Functions

- `generate_password()` - Generates a random password.
- `calculate_hash()` - Calculates the SHA-256 hash.
- `display_results()` - Displays the results.
- `generate_password_and_hash()` - Handles the program execution.

## Technologies

- Python
- Secrets
- String
- Hashlib

## Note

SHA-256 is a hashing algorithm, not encryption. This project is for learning and practicing password generation and hashing. For real password storage, dedicated algorithms such as Argon2 or bcrypt should be used.

## Author

Bashar Almadhaji

Cybersecurity Student | Python Programming
