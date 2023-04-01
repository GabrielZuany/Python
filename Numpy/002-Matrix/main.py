import numpy as np

matriz_diagonal1 = np.eye(3)
print(matriz_diagonal1)

print()

matriz_1 = np.array( [ [1, 2, 3],[4, 5, 6] ] )
print(matriz_1)
print(matriz_1.shape)

print()

matriz_2 = np.ones((2,3))
print(matriz_2)

print()

mylist = [ [22, 445, 65],[1, 54, 88],[99, 1, 0] ]
matriz_3 = np.matrix(mylist)
print(matriz_3)
print(matriz_3[2, 2])
print(matriz_3[0:2, 1])

print()
print()

matriz_3d = np.array([
    [
        [6, 7, 1],
        [9, 0, 21],
        [1, 4, 3]
    ],
    [
        [1, 11, 23],
        [91, 54, 33],
        [14, 44, 30]
    ]
    ])

print(matriz_3d)
print(matriz_3d.ndim)
print(matriz_3d.shape)

print()
print()

matriz_4d = np.array(
    [
        [   
            [
                [6, 7, 1],
                [9, 0, 21],
                [1, 4, 3]
            ],
            [
                [1, 11, 23],
                [91, 54, 33],
                [14, 44, 30]
            ]
        ],
        [
            [
                [6, 7, 1],
                [9, 0, 21],
                [1, 4, 3]
            ],
            [
                [1, 11, 23],
                [91, 54, 33],
                [14, 44, 30]
            ]
        ]
    ] 
    )

print(matriz_4d)
print(matriz_4d.ndim)
print(matriz_4d.shape)

print()
print()