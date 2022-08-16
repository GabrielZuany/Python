#Make a script that reads a number between 1000 and 9999 and prints unit ,ten ,hundred and thousand.
num = int(input('<<int>> Insert a number between 1000 and 9999:'))
string = str(input('<<str>> Insert a number between 1000 and 9999:'))

d1 = num%10
num = num//10
d2 = num%10
num = num//10
d3 = num%10
d4 = num//10
print('USING INT -> Un:{} , Ten:{} , Hundred:{} , Thousand:{}' .format(d1, d2, d3, d4))

un = string[3]
ten = string[2]
hun = string[1]
thou = string[0]
print('USING STR -> Un:{} , Ten:{} , Hundred:{} , Thousand:{}' .format(un, ten, hun, thou))