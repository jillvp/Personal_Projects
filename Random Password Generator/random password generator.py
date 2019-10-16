import random

chars = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ123456789!?,.-'

length = int(input('choose a password length: '))

password = ''

# choose a random character for the length entered:
for c in range(length):
    password += random.choice(chars)

print("Here is your password: \n" + password)
