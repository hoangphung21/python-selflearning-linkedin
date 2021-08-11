class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.loginAttemps = 0

    def describe_user(self):
        des = f"User's full name: {self.firstName} {self.lastName}."
        return des.title()

    def greeting_user(self):
        greeting = f"Hello {self.firstName}"
        return greeting.title()

    def increment_login_attemps(self):
        self.loginAttemps += 1
        return f"You logged in {self.loginAttemps} times"

    def reset_login_attemps(self):
        self.loginAttemps = 0
        return f"Attemps have been reset"


hoang = User('hoang', 'phung')
print(hoang.describe_user())
