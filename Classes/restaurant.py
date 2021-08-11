class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now opened")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'vanilla', 'hazelnut']

    def show_flavors(self):
        for i in range(len(self.flavors)):
            print(self.flavors[i])


anhdao = IceCreamStand('Anh Dao', 'South Vietnam')
anhdao.describe_restaurant()
anhdao.open_restaurant()
anhdao.show_flavors()
