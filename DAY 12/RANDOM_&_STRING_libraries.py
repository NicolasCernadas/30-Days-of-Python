from string import ascii_letters, digits, punctuation
from random import random, randint
print(ascii_letters)
print(digits)
print(punctuation)

print(random()) #return value from 0 to 0.999...
print(randint(5, 20)) #both included

#Example:

def generating_ID(name):
    ID = []
    key_ID = str()
    for i in range(0,5):
        number = randint(0,51)
        character = ascii_letters[number]
        number = randint(0,5)
        ID.append(character)
        ID.append(number)
        print(ID)
    for item in ID:
        key_ID += str(item)

    user = {
        'name': name,
        'ID' : key_ID
    }
    return str(user)

user_ID = generating_ID('Nicolas')
print(user_ID)

