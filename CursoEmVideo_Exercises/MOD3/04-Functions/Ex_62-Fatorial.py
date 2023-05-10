#Make a program to calculate a fatorial number and shows or not the calculation process. Also, build the function fat(V, SW) docstring.
def fat(num, show=False):
    """""
    Description: =>Calculate the fatorial of a number and shows (or not) the process.

    Args:
        num (int): number that will be calculated.
        show (bool, optional): if the user want to see the process. Defaults to False.

    Returns:
        int : result os (num)!
    """
    res = 1
    count = num
    while count>0:
        if show==True:
            print(f'{count}', end ='')
            if count != 1:
                print(' X ', end ='')
            else:
                print(' = ', end ='')
        res*= count
        count-=1
    return res

#---------MAIN---------
res = int(input('What number do you want to calculate fatorial? '))
show = str(input('Do you want to show the process? [Y/N]')).upper()
if show == 'Y':
    value = fat(res, True)
else:
    value = fat(res, False)
print(value)