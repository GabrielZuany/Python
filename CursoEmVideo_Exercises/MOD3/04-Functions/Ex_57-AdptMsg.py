#Build a program witch has a function called by 'write()' that recieves a mesage  and print the mesage formated with the apropriate size.
def write(msg):
    size = len(msg)+4
    print('*'*size)
    print(f'  {msg}',)
    print('*'*size)

word = input('Insert a text: ')
write(word)