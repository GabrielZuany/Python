#Develop a program that reads the first term and ratio of an arithmetic progression and displays the first 10 terms of the AP.
#an = a1 + (n-1).r

a1 = int(input('First term os AP: '))
ratio = int(input('AP ratio: '))

for n in range(1, 11, +1):
    an = a1 + (n-1)*ratio
    print('A{} = {}' .format(n, an))

print('END!')

