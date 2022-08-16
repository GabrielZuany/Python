#Make a script that reads 3 lines and print if they can build a triangle
r1 = float(input('Insert the first line: '))
r2 = float(input('Insert the second line: '))
r3 = float(input('Insert the third line: ' ))

if(r3 < r1+r2 and r2 < r1+r3 and r1 < r2+r3):
    print('You can build a triangle')
else:
    print('You cant build a triangle')