#Build a program with a function called 'area()', that receives the terrain (retangular) dimension and show the area.
def area(x, y):
    print(f'AREA = {x*y} m²')
def dif():
    print('*'*30)

dif()
x = float(input('X(m): '))
y = float(input('Y(m): '))
dif()
area(x, y)