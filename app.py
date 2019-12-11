# cryptokey is a random password generator
import random

characters = 'abcdefghijklmnopqrstuvwxyz1234567890'

select = input("how many passwords do you want to generate? ")
select = int(select)
length = input("length of password(s)? ")
length = int(length)

for i in range(select):
    for c in range(length):
        password = ''
        password += random.choice(characters)
        print(password, end = '')
    print(select)
