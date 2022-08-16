#Make a script to read the day, month and year that a person born and shows the formated date.
#Crie um script que leia o dia, mes e ano de uma pessoa e mostre a data formatada.

day = input('Day = ')
month = input('Month =  ')
year = input('Year = ')

print('You born in',day,'/',month,'',year)
#OR
print('You born in {}/{}/{}' .format(day, month, year))
