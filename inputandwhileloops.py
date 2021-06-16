# # HOW THE INPUT FUNCTION WORKS
# prompt = "What kind of car do you want?"
# car = input(prompt)
# print(car.title())

# # WORKING WITH WHILE LOOPS
# currentNumber = 1
# while currentNumber <= 5:
#     print(currentNumber)
#     currentNumber += 1
# # letting user choose when to quit
# prompt = "\nTell me something and I will try to reply ack to you"
# prompt += "\nEnter quit to exit the program: "
# message = ""
# while message.lower() != "quit":
#     message = input(prompt)
#     if message.lower() != "quit":
#         print(message)

# # USING WHILE LOOP WITH LISTS AND DICTIONARIES
# Moving item from one list to another
# unconfirmedUsers = ['alice', 'bob', 'david']
# confirmedUsers = []

# while unconfirmedUsers:
#     currentUser = unconfirmedUsers.pop()
#     print(f"Veryfying user: {currentUser.title()}")
#     confirmedUsers.append(currentUser)
# for confirmedUser in confirmedUsers:
#     print(confirmedUser.title())

# Removing all Instances of Specific Values from a list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# Filling a dictionary with user input
responses = {}
# set a flag to indicate that polling is activated
pollingActive = True
while pollingActive:
    # prompt for the person's name and response
    name = input("What is your name? ")
    response = input("What's your favorite country? ")
    # store the response in dictionary
    responses[name] = response
    # find out if anyone else is going to take a poll
    while True:
        repeat = input(
            "Would you like to let another person respond? (yes/ no) ")
        if repeat.lower() == 'no':
            pollingActive = False
            break
        elif repeat.lower() not in ('yes', 'no'):
            print("Invalid Input")
            True
        elif repeat.lower() == 'yes':
            pollingActive = True
            break
# Polling is completed, showing the result
for name, response in responses.items():
    print(f"{name}'s favorite country is {response}.")
