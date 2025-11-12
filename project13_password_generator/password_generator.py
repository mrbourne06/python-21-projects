import random
import string

def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = []
    # Ensure at least one number/special if required
    if numbers:
        pwd.append(random.choice(digits))
    if special_characters:
        pwd.append(random.choice(special))

    # Fill the rest randomly
    while len(pwd) < length:
        pwd.append(random.choice(characters))

    # Shuffle to mix guaranteed characters
    random.shuffle(pwd)

    return ''.join(pwd)

length = int(input('Enter the length of your desired password: '))
has_number = input('Do you want to have numbers (y/n)?').strip().lower() == 'y'
has_special = input('Do you want to have special characters (y/n)?').strip().lower() == 'y'
pwd = generate_password(length, has_number, has_special)
print(f'The generated password is: {pwd}')