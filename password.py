import random
import string
import pyperclip  # Required for copying to clipboard

def generate_password(length, uppercase, lowercase, numbers, special_characters):
    """Generate a random password with specified length and character types"""
    characters = ''
    password =''
    if uppercase == 'y':
        characters += string.ascii_uppercase
    if lowercase == 'y':
        characters += string.ascii_lowercase
    if numbers == 'y':
        characters += string.digits
    if special_characters == 'y':
        characters += string.punctuation

    if length != 0:
        for _ in range(length):
            password = password+(random.choice(characters))
    else:
        print("Length of password can't be zero")
        main()
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower()
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    special_characters = input("Include special characters? (y/n): ").lower()

    if uppercase == lowercase == numbers == special_characters == 'n':
        print("You must have to include atleast any one")
        main()
    else:
        password = generate_password(length, uppercase, lowercase, numbers, special_characters)
        print("Generated Password:", password)

    # Copy password to clipboard
    copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").lower()
    if copy_to_clipboard == 'y':
        pyperclip.copy(password)
        print("Password copied to clipboard!")

if __name__ == "__main__":
    main()

