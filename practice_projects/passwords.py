import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password =  ''.join(random.choice(characters) for _ in range(length))
    return password

while True:

    print(f'Your new password is: {generate_password()}')
    
    response = input('Would you like more passwords? Type y or n: ')
    if response == 'n':
        print(f"\nYou're good to go!")
        break