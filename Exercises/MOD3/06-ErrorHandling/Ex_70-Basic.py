try:
    a = int(input('a: '))
    b = int(input('b: '))
    r = a/b
except Exception as error:
    print(f'There was an error ({error.__class__}) executing the program.')
else:
    print(r)
finally:
    print('End of program...')