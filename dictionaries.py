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
customer1 = {
    'first_name': 'Hoang',
    'last_name': 'Phung',
    'age': 26,
    'city': 'Toronto'
}
print(customer1)

for keys, values in customer1.items():
    print(keys, ":", values)
