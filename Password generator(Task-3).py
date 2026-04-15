import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4!")
            return
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        all_chars = letters + digits + symbols

        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols)
        ]

        for _ in range(length - 3):
            password.append(random.choice(all_chars))

        random.shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Password:", final_password)

    except ValueError:
        print("Please enter a valid number!")

generate_password()