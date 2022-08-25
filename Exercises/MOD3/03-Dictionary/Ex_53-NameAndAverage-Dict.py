#Build a program to read 3 studants name and average, the calculate his situation. At the end, show the struct content. 
data = dict()
students = list()

for count in range(0, 3):
    data['name'] = str(input('Name: '))
    data['average'] = float(input(f'{data["name"]} average: '))
    students.append(data.copy())
    
    if students[count]['average'] >= 7:
        students[count]['situation'] = 'Approved'
    else:
        students[count]['situation'] = 'Disapproved'

print('*'*40)

for count in range(0, 3):
    print(f'Student {count+1} -> ', end='')
    for key, value in students[count].items(): 
        print(value, end='; ')
        
    print()