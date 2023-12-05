# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python to make an
# empty tuple called toppings and pack whatever values it receives into this tuple

# the parameter that accepts an arbitrary number of arguments must be placed last
def make_pizza1(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')

# **kwargs used to collect non-specific keyword arguments