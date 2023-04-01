import numpy as np

mylist = [10, 23, 34, 31, 2, 5, 89]

arr1 = np.array(mylist)

print(arr1)
print(type(arr1))
print(arr1.shape)

print(f"\n{arr1[1:4]}")
print(arr1[1:4+1])

idx = [1, 2, 4, 5]
print(arr1[idx])

mask = (arr1 % 2 == 0) # máscara booleana com os valores pares
print(f'\n{mask}')
print(arr1[mask])


mylist2 = [1, 2, 3, 4, 5]
arr2 = np.array(mylist2)

print(f"\nArray: {arr2}")
print(f"Soma acumulada: {arr2.cumsum()}") 
print(f"Produto acumulado: {arr2.cumprod()}") 

arr3 = np.arange(0, 50, 5) # cria uma lista de elementos -> start, stop, step
print(f"\nArray3: {arr3}")

arr4 = np.zeros(10)
print(f"\nArray4: {arr4}")

