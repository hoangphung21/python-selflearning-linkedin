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
def makeAlbum(artist, albumTitle, numberOfSongs=''):
    album = {'artist': artist, 'albumName': albumTitle}
    if numberOfSongs:
        album['numberOfSongs'] = numberOfSongs
        formattedAlbum = f"\n{artist} \n{albumTitle} \n{numberOfSongs}"

    else:
        formattedAlbum = f"\n{artist} \n{albumTitle}"
    return formattedAlbum


makingNewAlbum = True
while makingNewAlbum:
    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    albumTitle = input("Enter album title: ")
    if albumTitle == 'q':
        break
    newalbum = makeAlbum(artist, albumTitle)
    print(newalbum)
