#Make a script that contains a pre-defined fully numeric tuple (0-5) and reads a value came by standard input. Then sow the full number (2 ='two' ...)
NumTuple = ('zero', 'one', 'two', 'three', 'four', 'five')
InputNum = int(input('What number do you want to show(0-5)? '))

if 0 < InputNum > 5:
    while 0 < InputNum > 5:
        print('Invalid value.')
        InputNum = int(input('What number do you want to show(0-5)? '))

print(NumTuple[InputNum])