import random
import string

def generate_password():
    print("=== Random Password Generator ===")
    
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("Error: Length must be at least 8 characters. Try again.\n")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.\n")
    
    print("\nChoose character types to include (select at least 2):")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    selected_count = sum([use_upper, use_lower, use_digits, use_symbols])
    
    if selected_count < 2:
        print("Error: You must select at least 2 character types.")
        return
    
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    print(f"\nGenerated Password: {password}")

while True:
    generate_password()
    again = input("\nGenerate another password? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using the Password Generator!")
        break
