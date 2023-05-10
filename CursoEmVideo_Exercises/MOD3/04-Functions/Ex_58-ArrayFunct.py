#Make a script to read the bidimentional array (size came by stdin), the print the array formated. (Use function)

def ReadArray(lines, columns):
    matrix = list()
    temp = list()
    
    for l_count in range (0, lines):
        for c_count in range(0, columns):
            value = input(f'[{l_count} {c_count}]: ')
            temp.append(value)
        matrix.append(temp.copy())
        temp.clear()
    
    return matrix

def PrintArray(matrix, lines, columns):
    for l_count in range(0, lines):
        print('| ', end='')
        for c_count in range(0, columns):
            print(f'{matrix[l_count][c_count]:^5}', end=' | ')
        print()

#*********MAIN**********
lines = int(input('Number of lines: '))
columns = int(input('Number of columns: '))
matrix = list()
matrix = ReadArray(lines, columns)
PrintArray(matrix, lines, columns)