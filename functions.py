# # Multiple functions
# def describePet(type, name):
#     """Display information for a pet"""
#     print(f"I have a {type}, its name is {name.title()}")


# describePet('hamster', 'Choo')
# describePet('dog', 'Blue')

# # EXCERCISE 8.3
# def makeShirt(text='I Love Python', size='L'):
#     print(f"Size of the t shirt: {size}")
#     print(f"The text: {text}")


# # positional argument
# makeShirt('XL', 'Sheridan')
# # keyword argument
# makeShirt(size='XXL', text='HooRay')
# # default
# makeShirt('AHIHI COOl', 'M')
# makeShirt()

# # RETURN VALUES
# Making an argument optional
# def getFormattedName(fname, lname, mname=''):
#     if mname:
#         fullName = f"{fname} {lname} {mname}"
#     else:
#         fullName = f"{fname} {lname}"
#     return fullName.title()


# rockers = getFormattedName('Matt', 'Shadow')
# print(rockers)
# rockers = getFormattedName('James', 'The Rev', 'sullivan')
# print(rockers)

# Return a dictionary
# def buildPerson(fname, lname, age=None):
#     person = {'firstName': fname, 'lastName': lname}
#     if age:
#         person['age'] = age
#     return person
# user = buildPerson('Henry', 'Phung', 27)
# print(user)

# Using a Function with a While Loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     fname = input("Enter your first name: ")
#     if fname == 'q':
#         break
#     lname = input("Enter your last name: ")
#     if lname == 'q':
#         break
#     formattedName = get_formatted_name(fname, lname)
#     print(f"Hello {formattedName}!")

# Albums management
# def makeAlbum(artist, albumTitle, numberOfSongs=None):
#     album = {'artist': artist, 'albumName': albumTitle}
#     if numberOfSongs:
#         album['numberOfSongs'] = numberOfSongs
#         formattedAlbum = f"Artist: {artist} \nTitle: {albumTitle} \nNumber of songs:{numberOfSongs}"
#     else:
#         formattedAlbum = f"Artist: {artist} \nTitle: {albumTitle}"
#     return formattedAlbum


# makingNewAlbum = True
# while makingNewAlbum:
#     artist = input("Enter artist name: ")
#     if artist == 'q':
#         break
#     albumTitle = input("Enter album title: ")
#     if albumTitle == 'q':
#         break
#     newalbum = makeAlbum(artist, albumTitle)
#     print(newalbum)

# Passing a List
# def greetingUsers(names):
#     for name in names:
#         msg = f"Hello {name.title()}"
#         print(msg)


# userNames = ['clover', 'henry', 'bimbim']
# greetingUsers(userNames)

# Modifying a List in a Function
# unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
# completedModels = []
# Simulating printing each designs until none are left
# Move each designs into completedModels after printing
# while unprintedDesigns:
#     currentDesign = unprintedDesigns.pop()
#     print(f"Printing model: {currentDesign}")
#     completedModels.append(currentDesign)
# # Display all completed models
# print("\nThe following models have been printed:")
# for completedModel in completedModels:
#     print(completedModel.title())

# Reorganize above code by writing 2 functions


# def printModels(unprintedDesigns, completedModels):
#     while unprintedDesigns:
#         currentDesign = unprintedDesigns.pop()
#         print(f"Printing model: {currentDesign}")
#         completedModels.append(currentDesign)


# def showCompletedModels(completedModels):
#     print("\nThe following models have been printed:")
#     for completedModel in completedModels:
#         print(completedModel.title())

# unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
# completedModels = []
# # adding [:] to prevent a function from modifying a list
# printModels(unprintedDesigns[:], completedModels)
# showCompletedModels(completedModels)

# Passing an Arbitrary Number of Arguments
