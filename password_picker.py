import random
import string

adjectives =['smelly','slow','fat','orange','blue','white','proud','brave']
nouns = ['apple', 'dinosaur', 'ball',
 'toaster', 'goat', 'dragon',
 'hammer', 'duck', 'panda']
print('Welcome to Password Picker!')
while  True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 10)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s'%password)
    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
     break
