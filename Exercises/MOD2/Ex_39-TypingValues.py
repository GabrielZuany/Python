#Create a program that reads several integers. At the end of the run, show the average of the entered values, the highest and the lowest. The program should ask whether or not the user wants to continue typing numbers.

from cmath import inf

Higher = 0
Lower = inf
Flag = 'Y'
sum = 0
NumeberOfTerms = 0

while Flag == 'Y':
    num = int(input('Insert an integer number: '))
    sum+=num
    NumeberOfTerms+=1

    if num>Higher:
        Higher = num
    if num<Lower:
        Lower = num

    Flag = str(input('Do you want to continue typing numbers? [Y/N]')).upper()

print('Higher: {}\nLower: {}\nAverage: {:.2f}' .format(Higher, Lower, sum/NumeberOfTerms))
