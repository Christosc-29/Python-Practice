import random
import string

def get_length():
    while True:
        try:
            pass_length = int(input("Enter your desired password size: "))
            if pass_length > 0:
                return pass_length
            else:
                print("The length has to be a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

def allow_special_characters():
    while True:
        answer = input("Do you wish to include special characters in the password? (Y/N): ").strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        else:
            print("Please answer either Y/y or N/n .")

def generate_password(length, include_special):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    size = get_length()
    use_special = allow_special_characters()
    password = generate_password(size, use_special)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
