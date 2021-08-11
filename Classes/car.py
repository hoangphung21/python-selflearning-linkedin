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


class Battery:
    """A simple attemp to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 350
        print(f"This car can go about {range} in full charge")


class ElectricCar(Car):
    """Represnet aspects of a car, specific to electric vehicles"""
    """super() is used to call a method from parent class"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar('tesla', 'model S', 2019)
# print(my_tesla.get_descretive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
