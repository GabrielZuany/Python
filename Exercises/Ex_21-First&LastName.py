#Make a script that reads a name and prints the first and last name.

name = input('Insert your full name: ')
SplitedName = name.split(' ')

print('First name: {}' .format(SplitedName[0]))

lastNamePosition = len(SplitedName)-1
print('Last name: {}' .format(SplitedName[lastNamePosition]))