#Make a script that, after read 4 standard input values (insert them in a tuple), print the number of '9'; The position of first '3'; all odd numbers. 

n1 = int(input('Insert a number:'))
n2 = int(input('Insert another number:'))
n3 = int(input('Insert another number:'))
n4 = int(input('Insert last number:'))
Tuple = (n1, n2, n3, n4)

print('\nThe number ''9'' appears {} times' .format(Tuple.count(9)))
print('Odd numbers:', end='-> ')

for count in range (0,4):
    if Tuple[count]%2 == 0:
        print(Tuple[count], end = ' ')

if 3 in Tuple:
    print('\nFirst ''3'': {}' .format(Tuple.index(3)+1))
else:
    print('\nNumber 3 dont appear in Tuple')