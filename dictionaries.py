# # simple dictionaries

# # alien_0 = {'color': 'green', 'points': 5}
# # new_points = alien_0['points']
# # print(f"You just earn {new_points} points")


# # working with dictionaries
# # adding new key values
# # alien_0 = {'color': 'green', 'points': 5}
# # print(alien_0)

# # alien_0['x_position'] = 0
# # alien_0['y_position'] = 25

# # print(alien_0)

# # Starting witn an empty dictionaries
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'
# alien_0['speed'] = 'fast'
# print(alien_0)

# # now we move the alien to right by increasing the x
# # determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# # the new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# # removing key values
# del alien_0['points']
# print(alien_0)

# a dictionary of similar objects
# favourite_laguages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# language = favourite_laguages['sarah'].title()
# print(f"Sarah's favourite language is {language}")

# using get() to Access Values
# alien_0 = {'color': 'green', 'spped': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned')
# print(point_value)

# Excercies 1
# customer1 = {
#     'first_name': 'Hoang',
#     'last_name': 'Phung',
#     'age': 26,
#     'city': 'Toronto'
# }
# print(customer1)

# for keys, values in customer1.items():
#     print(keys, ":", values)

# looping through a dictionay
# favourite_laguages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# for name, language in favourite_laguages.items():
#     print(f"{name.title()}'s favorite language is: {language.title()}")
# # looping through values, using set to avoid duplicated values
# print("The languages have been mentioned are:")
# for language in set(favourite_laguages.values()):
#     print(language.title())
# # list of friends
# friends = ['phil', 'sarah', 'david', 'edward', 'jen', 'ani', 'hoang']
# for name in favourite_laguages.keys():
#     print(name.title())
#     if name in friends:
#         language = favourite_laguages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
# for friend in friends:
#     if friend in sorted(favourite_laguages.keys()):
#         print(f"{friend.title()}, thank you for taking the poll.")
#     else:
#         print(f"{friend.title()} please take the poll!")

# NESTING
# # a List of dictionaries
# import random

# colors = ['red', 'green', 'yellow', 'black', 'white', 'blue', 'pink']
# speed_types = ['slow', 'medium', 'fast']


# aliens = []

# for alien_number in range(30):
#     new_aliens = {'color': random.choice(colors),
#                   'points': random.randint(1, 10),
#                   'speed': random.choice(speed_types)}
#     aliens.append(new_aliens)
# # show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print(f"Total number of aliens: {len(aliens)}")

# # A list in a Dictionary
# Store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }
# # Summarize the order
# print(
#     f"You ordered a {pizza['crust'].title()} crust pizza with these following toppings:")
# for topping in pizza['toppings']:
#     print("\t"+topping)

# favourite_laguages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c', 'java'],
#     'edward': ['ruby'],
#     'phil': ['python', 'r']
# }
# for names, languages in favourite_laguages.items():
#     print(f"{names.title()}'s favourite laguages are:")
#     for language in languages:
#         print(f"\t {language.title()}")

# # A DICITONARY IN DICTIONARY
users = {
    'aeinstein': {
        'fname': 'albert',
        'lname': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'fname': 'marie',
        'lname': 'curie',
        'location': 'paris'
    }
}
for username, userInfo in users.items():
    print(f"Username: {username}")
    fullName = f"{userInfo['fname']} {userInfo['lname']}"
    location = userInfo['location']

    print(f"\tFull name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
