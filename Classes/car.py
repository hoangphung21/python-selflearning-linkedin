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
        self.odemeter_reading = mileage


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descretive_name())
my_new_car.read_odometer()

# # modifying an attribue's value directly
my_new_car.update_odemeter(23)
my_new_car.read_odometer()
