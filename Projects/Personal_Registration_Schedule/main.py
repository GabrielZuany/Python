import prs

data = dict()
schedule = list()
num = prs.NumberOfPeople()
file=open("InputData/file.txt", "r")
    
for n in range(0, num):
    data = prs.ReadData(data, file)
    schedule.append(data.copy())
    data.clear()

prs.BuildDataFrame(schedule)
