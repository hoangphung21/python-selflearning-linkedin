# cars = ['audi', 'subaru', 'toyota', 'honda', 'bmw']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# excercise 1
# import random

# color = ['red', 'blue', 'white', 'black', 'yellow']
# alien_color = random.choice(color)

# if alien_color == 'red':
#     print(f"You just kill a {alien_color.title()} alien")
# else:
#     print(f"You just kill a {alien_color.title()} alien")

# excercise 2:

current_users = ['hoangfbw', 'frozenAzure', 'wknancy', 'dinhta', 'jennyngo']
new_users = ['HOANGFBW', 'frozenazure', 'BimBim', 'dinhta', 'cloverhuynh']

upper_current_users = current_users[:]
upper_current_user = [user.upper() for user in upper_current_users]
print(upper_current_user)

lower_current_users = current_users[:]
lower_current_user = [user.lower() for user in lower_current_users]
print(lower_current_user)


for user in new_users:
    if user in current_users:
        print(f"{user} is not avaiable")
    elif user.upper() in upper_current_user:
        print(f"{user} is not avaiable")
    elif user.lower() in lower_current_user:
        print(f"{user} is not avaiable")
    else:
        print(f"{user} is avaiable")
