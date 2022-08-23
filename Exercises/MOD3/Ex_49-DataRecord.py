#Build a script that reads the name and weight (use list) of a group (size non defined). Ate the end, show how many people was recorded, a list with the heavier people and lighter people. (>90 heavy; <70 light)
data = list()
group = list()
keep = 'Y'

while keep == 'Y':
    data.append(str(input('Name: ')))
    data.append(float(input('Weight: ')))
    group.append(data[:])
    data.clear()
    
    keep = str(input('Do you want to keep recording data? [Y/N]')).upper()
    
print('\nHeaviest: ', end='')
for info in group:
    if info[1] > 90:
        print(f'{info[0]}, { info[1]:.1f} Kg',  end='// ')
        
print('\nLighter: ', end='')
for info in group:
    if info[1] < 70:
        print(f'{info[0]}, { info[1]:.1f} Kg',  end='// ')
        
print()
            