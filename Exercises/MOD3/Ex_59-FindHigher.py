#from a sequence of values(while user do not insert '999'), find the high number and quantity of values(use function).
def readval(values):
    values = list()
    
    while True:
        num = int(input('-> '))
        if num==999:
            break
        
        values.append(num)
        
    return values
    
def findHigher(lst):
    size = len(lst)
    higher = 0
    
    for count in range(0, size):
        if lst[count] > higher:
            higher = lst[count]
            
    print('-'*30, '\nHIGHER = {}' .format(higher))
    
#****************MAIN*******************
values = list()
values = readval(values)
print(f'You have inserted {len(values)} numbers.')
findHigher(values)