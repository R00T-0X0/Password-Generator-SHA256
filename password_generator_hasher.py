
import secrets
import string
import hashlib


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    digit = secrets.choice(string.digits)
    symbol = secrets.choice(string.punctuation)

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [uppercase, lowercase, digit, symbol]

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def calculate_hash(text):
    encoded_text = text.encode("utf-8")

    hash_value = hashlib.sha256(encoded_text).hexdigest()

    return hash_value


def display_results(password, hash_value):
    print("\n" + "=" * 45)
    print("       PASSWORD GENERATOR & SHA-256")
    print("=" * 45)

    print(f"Generated Password : {password}")
    print(f"SHA-256 Hash        : {hash_value}")

    print("=" * 45)


def generate_password_and_hash():
    try:
        length = int(input("Enter password length: "))

        password = generate_password(length)

        hash_value = calculate_hash(password)

        display_results(password, hash_value)

    except ValueError as error:
        print(f"[!] Error: {error}")


if __name__ == "__main__":
    generate_password_and_hash()
