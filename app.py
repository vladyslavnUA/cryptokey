# cryptokey is a random password generator
import random
from random import choice

characters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = characters.upper()
numbers = '0123456789'
symbols = '!@#$%&*()[]{}'

#for i in range(null):
    #password = ''
    #for b in range(length):
        #chars = random.choice(characters) + random.choice(uppercase_chars) + random.choice(numbers) + random.choice(symbols)
        #password += (chars)
        #print(password, end = '')
    #print(select)
    
def createPassword():
    charss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    AmountOfPasswords = int(input('how many passwords do you want to generate? '))
    lengthh = int(input('length of password(s)? '))

    while True:
        AmountOfPasswords = int(input('how many passwords do you want to generate? '))
        lengthh = int(input('length of password(s)? '))
        
    for i in range(0, AmountOfPasswords):
        passwordd = ''
        for c in range(lengthh):
            mixedchars = random.choice(characters) + random.choice(uppercase_chars) + random.choice(numbers) + random.choice(symbols)
            passwordd = ''.join(random.choice(mixedchars))
            print(passwordd)
        break
createPassword()
