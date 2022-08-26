#Develop a program that simulate a personal registration schedule (name, adress, ZIP code and phone). 
#To run, you can -> ~python3 main.py /// OR ~python3 main.py < InputData/file.txt
#The output will be find at 'RecordedData/file.txt'

REC = 80 #Number of records.
from ast import arg
import sys
import os
import builtins

#===============FUNCTIONS================
def SysConfig(status):
    archive = 'RecordedData/file.txt'
    if status == 1:#---------------------------if the archive is beeing written.
        sys.stdout = open(archive, 'a')
    elif os.path.exists(archive) == False:#-----if the output archive does not exists, create one.
        sys.stdout = open(archive, 'x')
    else:
        sys.stdout = open(archive, 'w')

def ReadData():        
    sys.stdout = open('temp.txt', 'w')#Do not print de below inputs at archive.
    data['name'] = str(input('Name: '))
    data['city'] = str(input('City: '))
    data['ZIP'] = int(input('ZIP code: '))
    data['phone'] = int(input('Phone number: '))
    os.remove('temp.txt')
    SysConfig(1)#---------------------Reset the output to main archive.
    return data

def PrintSchedule():#-----------------Print the header of schedule.
    print('-'*120)
    print(' '*40, 'PERSONAL REGISTRATION SCHEDULE')
    print('-'*120)
    print('INDEX','|', ' '*10, 'NAME',  ' '*10,'|', ' '*10, ' CITY ', ' '*10,'|', ' '*10, 'ZIP CODE',  ' '*10,'|', ' '*5, 'PHONE')
    print('-'*120)

def PrintInfo(data):#-------------------Print the current data.
    print(f"{data['name'] :^28}", end='|')
    print(f"{data['city'] :^30}", end='|')
    print(f"{data['ZIP'] :^32}", end='|')
    print(f"{data['phone'] :^19}", end='|')
    
#======================================

#--------------MAIN------------------------
data = dict()
schedule = list()
QuantityOfPeople = 5
SysConfig(0)
    
for index in range(0, REC):
    data = ReadData()
    schedule.append(data.copy())
    data.clear()

PrintSchedule()
for count in range(0, REC):
    print(f'{count :^5}', end = '|')
    PrintInfo(schedule[count])
    print()
    
print('-'*120)