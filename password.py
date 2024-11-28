# Take password input from the user
password = input("Enter your password: ")

# Minimum length check
if len(password) < 8:
    print("Your password is weak. It must be at least 8 characters long.")
else:
    # Initialize flags for different checks
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    # Check each character of the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    # Check if all conditions are met
    if has_uppercase and has_lowercase and has_digit and has_special:
        print("Your password is strong!")
    else:
        print("Your password is weak. Make sure it meets the following criteria:")
        if not has_uppercase:
            print("- Contains at least one uppercase letter.")
        if not has_lowercase:
            print("- Contains at least one lowercase letter.")
        if not has_digit:
            print("- Contains at least one digit (0-9).")
        if not has_special:
            print("- Contains at least one special character (e.g., !, @, #, $, %).")
