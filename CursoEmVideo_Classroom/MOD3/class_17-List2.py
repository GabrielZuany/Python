test1 = list()
test1.append('Gabriel')
test1.append(20)

test2 = list()
test2.append(test1[:])#copy

test1[0] = 'Isadora'
test1[1] = 19
test2.append(test1[:])#copy
#print(test2)

test3 = [['Gabriel', 20], ['Isadora', 19], ['Sofia', 17]]
'''print(test3[0]) # -> Gabriel, 20
print(test3[1]) # -> Isadora, 19
print(test3[2]) # -> Sofia, 17
print(test3[0][0]) # -> Gabriel
print(test3[0][1]) # -> 20
print(test3[1][0]) # -> Isadora
print(test3[1][1]) # -> 19
print(test3[2][0]) # -> Sofia
print(test3[2][1]) # -> 17'''

for data in test3:
    print(data[0])#only names
for data in test3:
    print(data[1])#only ages
    
for i in range(0, len(test3)):#Names and age
    for j in range (0, len(test3[0])):
        print(test3[i][j], end =' ')
    print()


info = list()#aux struct
group = list()#definitive struct

for count in range(0,3):
    info.append(str(input('Name: ')))
    info.append(int(input('Age: ')))
    group.append(info[:])#data copy
    info.clear()
print(group)