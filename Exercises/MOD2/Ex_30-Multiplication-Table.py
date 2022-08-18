#make a script that prints the multiplication table (1-10) of a real number (n).
num = float(input('Insert a number: '))

for count in range(1, 11, +1):
    print('1 X {} = {:.2f}' .format(num, num*count))
