n1 = float(input('Insert your fist test grade: '))
n2 = float(input('Insert your second test grade: '))
average = (n1+n2)/2

if (average>=7):#no need to use ()
    print('Approved with {:.2f}' .format(average))
else:
    print('Disapproved with {:.2}' .format(average))

print('\nEnd of execution.')