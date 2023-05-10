FirstGrade = 5.0
SecondGrade = float(input('2nd grade:'))
if((FirstGrade+SecondGrade)/2 >= 7):
    print('Approved')
elif (FirstGrade+SecondGrade)/2 >= 6 and (FirstGrade+SecondGrade)/2 <7:
    print('Almost approved')
else:
    print('Repproved')