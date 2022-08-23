#Create a matrix 3x3 with values readed by stdin (strandard input - terminal)

#READING A MATRIX N x M 
matrix = [[0, 0, 0], [0 ,0, 0], [0, 0, 0]]

for lines in range (0, 3):
    for columns in range(0, 3):
        matrix[lines][columns] = int(input(f'Insert a value to ({lines}, {columns}) -> '))
        
print('-'*22)
for lines in range (0, 3):
    for columns in range(0, 3):
        print(f'[{matrix[lines][columns]:^5}]', end = '')
    print()

print('-'*22)

'''ANOTHER WAY TO READ A MATRIX

matrix = list()
temp = list()

for lines in range (0, 3):
    for columns in range(0, 3):
        temp.append(int(input('-> '))) # ->Temporarily store the column values
        
    matrix.append(temp[:]) # ->Copy the columns values stored in temp
    temp.clear()
'''  