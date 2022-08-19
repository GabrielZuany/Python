#Make a script to calculate the fatorial of a number.

num =  int(input('Insert an integer number: '))
fat = 1

for num in range(num, 0, -1):
    fat = fat*num
print(fat)