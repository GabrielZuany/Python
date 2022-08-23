'''
Problem: Write a program to read a sequence of N numbers
for a vector and look for the first occurrence of a number X in that vector.
• Input: 1 integer X to search for, an integer N representing the
number of numbers, followed by N integers, all separated by spaces.
• Output: Index of the first occurrence of X in the vector, or the size of the vector if it is not
be present.'''
number = int(input(''))
size = int(input(''))
array = list()
resp = -1
for count in range(0, size):
    array.append(int(input('')))
for count in range(0, size):
    if array[count] == number:
        resp=count
        break
if resp == -1:
    resp = len(array)
print(f'RESP:{resp}', end='')