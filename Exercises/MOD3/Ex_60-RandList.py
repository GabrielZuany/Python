#Make a script that have a list builded with random numbers (function: 'randomise()'). Then make a functiont to sum only the even values of list(function: 'sum()').
from random import randint

def randomise():
    size = randint(1, randint(1, 10))
    lst = list()
    for count in range(0, size):
        value = randint(0, 10)
        lst.append(value)
        
    return lst
    
def sumEven(lst):
    sum = 0
    for value in lst:
        if value%2==0:
            sum+=value
    return sum
    
#*************MAIN************
lst = list()
lst = randomise()
sum = sumEven(lst)
print(f'The sequence generated is: {lst}')
print('*'*60)
print(f'The sum of even number is: {sum}')