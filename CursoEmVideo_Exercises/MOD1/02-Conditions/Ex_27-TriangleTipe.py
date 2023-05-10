#Make a script that reads 3 lines and print if they can build a triangle. If they can build the 
#triangle, your script must print the tipe of triangle (isosceles, equilateral or scalene).
r1 = float(input('Insert the first line: '))
r2 = float(input('Insert the second line: '))
r3 = float(input('Insert the third line: ' ))

if(r3 < r1+r2 and r2 < r1+r3 and r1 < r2+r3):
    
    if r1 in (r2, r3) or r2 in (r1, r3) or r3 in (r1, r2):
        print('Your triangle is isosceles')
    elif r1!=r2 and r2!=r3:
        print('Your triangle is scalene')
    elif r1 == r2 == r3:
        print('Your triangle is equilateral')

else:
    print('You cant build a triangle')