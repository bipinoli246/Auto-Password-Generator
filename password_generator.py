import random
import string

def generate_password(min_length, use_numbers=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if use_numbers:
        characters += digits
    if use_special:
        characters += special

    while True:
        password = ''.join(random.choice(characters) for _ in range(min_length))

        # Check that password meets chosen criteria
        if use_numbers and not any(c in digits for c in password):
            continue
        if use_special and not any(c in special for c in password):
            continue

        return password


# ---- Run the program ----
while True:
    try:
        min_length = int(input("Enter the minimum password length: "))
        break
    except ValueError:
        print(" Please enter a valid number!\n")

use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

password = generate_password(min_length, use_numbers, use_special)
print("\nGenerated Password:", password)
