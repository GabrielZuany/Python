string = 'Teeeest striing 1 2 3'
print(string)

print(string[3])

print(string[2:13])

print(string[:13])

print(string[3:])

print(string[2::2])

print(string[::2])

print(string.count('e'))

print(string.count('e', 0, 13))#Counts the number of 'e' in the string from 0 to 13

print(string.upper())#Converts the string to upper case

print(string.lower().count('i'))#Counts the number of 'i' in the string after converting it to lowercase

print(len(string))#Length of the string

print(string.replace('Teeeest', 'Hellooo'))#Replaces the string with the new string

print(string.replace('e', 'A'))#Replaces all the 'e' with 'A'

print(string)
string = string.replace('e', 'A')#Replaces all the 'e' with 'A'
print(string)

print(string.find('striing'))#Finds the index of the string
print(string.find('STriing'))#Finds the index of the string
print(string.upper().find('STRIING'))#Finds the index of the string

splited = string.split(' ')#Splits the string into a list
print(splited)

print(splited[0])#Prints the first element of the list
print(splited[0][5])#Prints the sixth element of the first element of the list