def greet_user(name):
    """Takes your name and
    prints a welcome message"""

    print(f"Welcome {name.title()}! Enjoy your stay.")

greet_user('eliud')

# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword Arguments

# Free you from having to worry about correctly ordering your arguments in the function call.
# They clarify the role of each value in the function call.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='cat', pet_name='minute')
describe_pet(pet_name='messi', animal_type='goat')

# default values
# You can use default values to make an argument optional
def describe_pets(pet_name, animal_type='dog'):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pets(pet_name='mike')
# To describe an animal other than a dog, you could use a function call
describe_pets(pet_name='larry', animal_type='dove')

def make_shirt(size, message):
    """graphic tee"""

    print(f"The shirt size{size} has a print:")
    print(f"{message.capitalize()}")

make_shirt('large', 'anarchy')

