# imported libraries
import random
import string
import re


# checks certain criteria to be met
def check_password_length(Password):
    if Password < 10:  # length of password minimum
        return "password is too short!"
    if not re.search(r"[A-Z]", Password):  # checks for uppercase letter in password
        return "password must have a uppercase letter"
    if not re.search(r"[a-z]", Password):  # checks for lowercase letter in password
        return "password must have a lowercase letter"


# generates a random password
# /\ follows parameter set by previous functions /\
def generate_password(length: int = 10):  # can edit to more or less
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password


password = generate_password()
print(f"Generated password: {password}")
