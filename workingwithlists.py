friends = ['ross', 'joey', 'chandler', 'phoebe', 'rachel', 'monica']
# for friend in friends:
#     print(friend)

# print(f"I can't wait to see {friend.title()}")

# trying numerical lists
# for value in range(1, 5):
#     print(value)
# numbers = list(range(1, 10))
# print(numbers)

# adding 2 after each number until reaching the end
# even_numbers = list(range(2, 20, 2))
# print(even_numbers)

# testing squares
# squares = []
# for value in range(1, 10):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# # simple static with those numbers
# print(f"The sum of lists: {sum(squares)}")
# print(f"The min of lists: {min(squares)}")
# print(f"The max of lists: {max(squares)}")

# # a shorter way
# squares1 = [value**2 for value in range(1, 11)]
# print(squares1)

# working with part of a list
# print(friends[1:4])
# print(friends[:3])
# print(friends[2:])
# print(friends[-3:])

# # looping through a slice
# print("Here are the 1st 3 people of Friends")
# for friend in friends[:3]:
#     print(friend.title())

# copying a list
# friends_copied = friends[:]
# print(friends_copied)
# friends.append('gunther')
# friends_copied.append('janice')
# print(friends)
# print(friends_copied)

# tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (500, 10)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
