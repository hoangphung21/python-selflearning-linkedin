# # Passing an Arbitrary Number of Arguments
def makePizza(size, *toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
