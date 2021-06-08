bikes = ['trek', 'asama', 'ncm', 'leon']
# print(bikes[0].title())
# message = f"My 1st bike was a {bikes[0].title()}"
# print(message)

# append can add a value into the last place of the list
# bikes.append('hooda')
# # print(bikes)

# # insert can be used to add to any places you want
# bikes.insert(0, 'wadas')
# print(bikes)

# # using pop
# poped_bike = bikes.pop()
# print(bikes)
# print(poped_bike)

# pop an exact position
# print(bikes)
# first_owned = bikes.pop(0)
# print(f"My first bike was a {first_owned.title()}")
# print(bikes)

# remove item by value
# print(bikes)
# bikes.remove('asama')
# print(bikes)

# sorting alphabet
bikes.sort()
print(bikes)
bikes.sort(reverse=True)
print(bikes)
