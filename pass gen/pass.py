import random
import string

def generate_password(length):
    # Define character sets
    digits = string.digits
    locase_char = string.ascii_lowercase
    upcase_char = string.ascii_uppercase
    symbols = '!@#$%&*_+'

    # Combine character sets
    combined_list = digits + upcase_char + locase_char + symbols

    # Ensure at least one character from each set
    rand_digit = random.choice(digits)
    rand_upper = random.choice(upcase_char)
    rand_lower = random.choice(locase_char)
    rand_symbol = random.choice(symbols)

    # Combine randomly selected characters
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # Fill the rest of the password length randomly
    for _ in range(length - 4):
        temp_pass += random.choice(combined_list)

    # Shuffle the password to randomize
    temp_pass_list = list(temp_pass)
    random.shuffle(temp_pass_list)

    # Generate final password
    password = ''.join(temp_pass_list)
    return password

def main():
    print("Welcome to Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Length should be at least 4.")
        else:
            password = generate_password(length)
            print("Your generated Password is:")
            print(password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
