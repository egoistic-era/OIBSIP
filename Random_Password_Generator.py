import random
import string

def create_password(length, use_digits, use_symbols):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    char_pool = letters

    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        size = int(input("Enter password length: "))

        if size < 4:
            print("Password length should be at least 4.")
            return

        digits_choice = input("Include numbers? (yes/no): ").lower() == "yes"
        symbols_choice = input("Include symbols? (yes/no): ").lower() == "yes"

        final_password = create_password(size, digits_choice, symbols_choice)

        print("\n--- Generated Password ---")
        print(final_password)

    except ValueError:
        print("Invalid input! Please enter correct values.")

# Run program
main()
