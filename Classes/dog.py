class Dog:
    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("Willy", 4)
print(f"My dog's name is {my_dog.name}")
print(f"He is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()
