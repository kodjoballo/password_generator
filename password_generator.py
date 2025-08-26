# Password Generator

import random

import string
from operator import truediv


# password generator as per the way the user wants it (letters, symbols, digits)

def generate_password(min_length, numbers = True, special_character = True):

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd

length = int(input("What is the wanted length of the password: ?"))
numb = input("Do you want the password to include numbers: ").lower() == "y"
spec = input("Do you want the password to include special character: ").lower() == "y"

password = generate_password(length, numb, spec)

print(f"Your password is {password}")






