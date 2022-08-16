#Make a script that asks the user name and then prints the name uppercased and lowercased.Also print the number of characters (without whitespaces) in the name and the lenght of first name.

name = input('Insert your name: ')
print('The name uppercased is: {}' .format(name.upper()))
print('The name lowercased is: {}' .format(name.lower()))
print('The number os charachters of name is: {}' .format(len(name)))

name = name.split(' ')
print('The number of letters of name is: {}' .format(len(name[0]) + len(name[1])))
print('The length of first name is: {}'.format(len(name[0])))