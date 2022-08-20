l = list(range(1, 10))
print(l)

l.sort(reverse=True)
print(l)

l.append(111)#insert at end of list the number 111
print(l)

l.remove(111)#remove from list the number 111 (no matter the position of 111)
print(l)

l[0] = 1234
print(l)

l.insert(1, 1699)#insert(position, value)
print(l)

l.sort()
print(l)
l.pop()#remove the last item
print(l)

l.pop(5)#remove 5th item
print(l)

l.append(2)
l.remove(2)#remove the first '2'
print(l)

'''array = list()
for count in range (0,5):
    array.append(int(input('Insert an integer number:')))
print(array)'''

print('\nLINKED LIST:')
a = [0, 0, 0, 0]
b = a #LINK B <-> A, INSNOT A COPY!!!
b[2] = 1
print(f'A -> {a}')
print(f'B -> {b}')

print('COPY LIST:')
a = [0, 0, 0, 0]
b = a[:] #COPY ALL A ELEMENTS TO B!
b[2] = 1
print(f'A -> {a}')
print(f'B -> {b}')