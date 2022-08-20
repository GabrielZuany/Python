Tuple = ('item 1', 'item 2', 'item 3')
print(Tuple)

for item in Tuple:
    print(f'{item}')

print()

for count in range(0, len(Tuple)):
    print(f'{Tuple[count]}')

print('~'*30)

a = (1, 5, 7)
b = (9, 5, 4, 9)
c = a+b
d = b+a
print(f'a = {a}; b = {b}; c = a+b; d = b+a')
print(f'c = {c}\nd = {d}')

del(c, d)