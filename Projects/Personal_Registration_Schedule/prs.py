import sys
import os
import pandas as pd
import mmap


def NumberOfPeople():
    """
    Returns the number of people to be recorded accord to the number of lines in file.txt. 

    Returns:
        int: number of records
    """
    with open('InputData/file.txt', "r+") as myfile:
        mm = mmap.mmap(myfile.fileno(), 0)
        total_lines = 0

        while mm.readline():
            total_lines += 1
    return int(total_lines/4)


def ReadData(data, file):      
    """
    Read the input file.

    Args:
        data (dict): dict to be append into a list.

    Returns:
        dict: dict to be append into a list.
    """
    data['name'] = file.readline()
    data['city'] = file.readline()
    data['ZIP'] = file.readline()
    data['phone'] = file.readline()
 
    return data

def BuildDataFrame(schedule):
    """
    Build a DataFrame to store the data into a .xlsx file.

    Args:
        schedule (dict): colleted data.
    """
    df = pd.DataFrame(schedule, columns=['name', 'city', 'ZIP', 'phone'])
    df.to_excel("RecordedData/file.xlsx", index=False)


    