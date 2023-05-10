from random import randint

def printmsg(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
    
def sum(a, b):
    print(a+b)
    
def count(*num):
    lenght = len(num)
    print(f'Size = {lenght} -> {num}')

def multvalues(lst, mult):
    pos = 0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

#*********MAIN***********
printmsg('HELLO WORLD')
printmsg(5)

sum(8, 7)
sum(100, 7)

count(0, 9)
count(9, 9, 8, 1, 4)

values = [2, 5, 7, 9, 14]
mult = 2
print(values, end='->')
multvalues(values, mult)#Modify the list (like array in C) -> PY use reference param. 
print (values)