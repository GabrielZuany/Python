#make a script that calculates the sum of all odd numbers and multiples of 3 between 1 and 500.
sum = 0

for count in range(0, 500, +3):
    if(count%3 == 0 and count%2 != 0):
        sum+=count
        print('{} + ' .format(count))

print('Sum: {}' .format(sum))