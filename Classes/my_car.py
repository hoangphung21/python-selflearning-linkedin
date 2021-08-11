from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descretive_name())


my_new_car.odemeter_reading = 23
my_new_car.read_odometer()
