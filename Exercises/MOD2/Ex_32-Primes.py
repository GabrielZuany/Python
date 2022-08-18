#develop a program that reads an open interval (n-m) and prints all the prime numbers in that interval.
import math
StartOfRange = int(input('Start of range: '))
EndOfRange = int(input('End of range: '))
flag = 0

for num in range(StartOfRange+1, EndOfRange, +1):
    
    for count in range(1, num+1, +1):
        if num%count == 0:
            flag+=1

    if flag == 2:
        print('-> {}' .format(num))
    
    flag = 0
