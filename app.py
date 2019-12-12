# cryptokey is a random password generator
import random
from random import choice

characters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = characters.upper()
numbers = '0123456789'
symbols = '!@#$%&*()[]{}'

for i in range(select):
    password = ''
    for b in range(length):
        chars = random.choice(characters) + random.choice(uppercase_chars) + random.choice(numbers) + random.choice(symbols)
        password += (chars)
        print(password, end = '')
    print(select)


#def password():
    #pchars = random.choice(characters)
    #psymbols = random.choice(symbols)
    #pnumbers = random.choice(numbers)
    #pupper = random.choice(uppercase_chars)
    #crypto_password = str(pchars) + str(psymbols) + str(pnumbers) + str(pupper)
    #return crypto_password

charss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
AmountOfPasswords = int(input('how many passwords do you want to generate? '))
lengthh = int(input('length of password(s)? '))

for p in range(AmountOfPasswords):
    passwordd = ''
    for c in range(0, lengthh):
        passwordd += random.choice(charss)
    print(passwordd)
