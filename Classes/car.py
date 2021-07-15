class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # set a defalut value for an attribute
        self.odemeter_reading = 0

    def get_descretive_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odemeter_reading} km on it")

    def update_odemeter(self, mileage):
        # modifying an attribute's value through a methodß
        if mileage >= self.odemeter_reading:
            self.odemeter_reading = mileage
        else:
            print("You cant roll back an odometer")

    def increment_odometer(self, miles):
        self.odemeter_reading += miles

# Inheritance; init method in a child class


class ElectricCar(Car):
    """Represnet aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descretive_name())
