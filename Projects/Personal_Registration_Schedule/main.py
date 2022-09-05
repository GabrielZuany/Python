#Develop a program that simulate a personal registration schedule (name, adress, ZIP code and phone). 
#To run, you can -> ~python3 main.py /// OR ~python3 main.py < InputData/file.txt
#The output will be find at 'RecordedData/file.txt'

REC = 80 #Number of records.
import sys
import os
#===============FUNCTIONS================
def SysConfig():
    archive = 'RecordedData/file.txt'
    if os.path.exists(archive) == False:#if the output archive does not exists, create one.
        sys.stdout = open(archive, 'x')
    else:
        sys.stdout = open(archive, 'w')

def ReadData():       
    data['name'] = str(input(''))
    data['city'] = str(input(''))
    data['ZIP'] = str(input(''))
    data['phone'] = str(input(''))
    return data

def PrintSchedule():#Print the header of schedule.
    print('-'*120)
    print(' '*38, 'PERSONAL REGISTRATION SCHEDULE')
    print('-'*120)
    print('INDEX|', ' '*10, 'NAME',  ' '*10,'|', ' '*10, ' CITY ', ' '*10,'|', ' '*10, 'ZIP CODE',  ' '*10,'|', ' '*5, 'PHONE')
    print('-'*120)

def PrintInfo(data):#Print the current data.
    print(f"{data['name'] :^28}", end='|')
    print(f"{data['city'] :^30}", end='|')
    print(f"{data['ZIP'] :^32}", end='|')
    print(f"{data['phone'] :^19}", end='|')
    
#======================================

#-----------------MAIN---------------------
data = dict()
schedule = list()
SysConfig()
    
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
