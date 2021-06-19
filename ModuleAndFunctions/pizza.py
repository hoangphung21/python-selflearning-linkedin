# # Passing an Arbitrary Number of Arguments
def makePizza(size, *toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


makePizza('L', 'green onions',)
makePizza('XL', 'shooms', 'cheese', 'grilled chicken')
