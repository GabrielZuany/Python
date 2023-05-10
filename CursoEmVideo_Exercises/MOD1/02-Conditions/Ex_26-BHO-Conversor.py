#Make a script that asks the user a number and convert it to binary, Hex or Octal sistem numeration.
num = int(input('Insert a number: '))
option = int(input('Choose an option: \n1)Binay\n2)Hex\n3)Octal\n'))

if option == 1:
    print('{} in binary is {}' .format(num, bin(num)))
    #if you do not want the prefix 0b use: bin(num)[2:]
elif option == 2:
    print('{} in hex is {}' .format(num, hex(num)))
    #if you do not want the prefix 0x use: hex(num)[2:]
elif option == 3:
    print('{} in octal is {}' .format(num, oct(num)))
    #if you do not want the prefix 0o use: oct(num)[2:]
else:
    print('Invalid option')