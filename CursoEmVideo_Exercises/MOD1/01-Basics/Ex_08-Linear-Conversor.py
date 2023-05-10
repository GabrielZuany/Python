#Make a program tha reads a value in meters and display the correspondent value in centimeters and milimeters.
#Crie um programa que leia um valor em metros e exiba ele em centimetros e milimetros 

meters = float(input('Insert a value:'))
print('{} meters = {} cm e {} mm' .format(meters, meters*100, meters*1000))
